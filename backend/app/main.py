import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from graph.graph import build_graph
from schemas import ChatRequest, ChatResponse

logger = logging.getLogger(__name__)

_graph = build_graph()


@asynccontextmanager
async def lifespan(app: FastAPI):
    if not settings.anthropic_api_key and not settings.openai_api_key:
        logger.warning(
            "No cloud LLM API key configured. "
            "Requests will fail if Ollama is unreachable."
        )
    yield


app = FastAPI(
    title="PonchoProphet API",
    description=(
        "AI-powered outfit recommendations based on real-time weather data. "
        "Powered by Open-Meteo (weather) and Anthropic Claude (LLM)."
    ),
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins_list,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


def _format_weather_summary(weather: dict) -> str:
    return (
        f"{weather['temperature']}{weather['unit_temperature']}, "
        f"{weather['weather_description']}, "
        f"{weather['precipitation_probability']}% rain"
    )


@app.get("/health", tags=["meta"])
async def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse, tags=["chat"])
async def chat(request: ChatRequest):
    """
    Errors:
        422 — location string could not be geocoded
        503 — external service (weather API or LLM) unreachable
        500 — unexpected pipeline failure
    """
    initial_state = {
        "session_id":  request.session_id,
        "location":    request.location,
        "description": request.message,
    }

    try:
        final_state = await _graph.ainvoke(initial_state)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    except (ConnectionError, TimeoutError, OSError) as exc:
        raise HTTPException(status_code=503, detail=f"External service unavailable: {exc}")
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Pipeline error: {exc}")

    return ChatResponse(
        session_id=     request.session_id,
        answer=         final_state["answer"],
        weather_summary=_format_weather_summary(final_state["weather"]),
        cache_hit=      final_state.get("cache_hit", False),
    )
