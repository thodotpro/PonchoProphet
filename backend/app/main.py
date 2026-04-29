# backend/app/main.py
# FastAPI application — entry point for the backend.
# Run locally:  uvicorn app.main:app --reload  (from the backend/ directory)
# In Docker:    uvicorn app.main:app --host 0.0.0.0 --port 8000

from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from graph.graph import build_graph
from schemas import ChatRequest, ChatResponse


# ---------------------------------------------------------------------------
# Lifespan: runs once at startup and once at shutdown
# ---------------------------------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan hook for startup and shutdown."""
    yield
    # Nothing to tear down


# ---------------------------------------------------------------------------
# App instance
# ---------------------------------------------------------------------------

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
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _format_weather_summary(weather: dict) -> str:
    """Build a short, human-readable weather string for the UI status bar."""
    return (
        f"{weather['temperature']}{weather['unit_temperature']}, "
        f"{weather['weather_description']}, "
        f"{weather['precipitation_probability']}% rain"
    )


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.get("/health", tags=["meta"])
async def health():
    """Simple liveness probe — useful for docker-compose depends_on checks."""
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse, tags=["chat"])
async def chat(request: ChatRequest):
    """
    Main endpoint. Accepts a location (and optional style description),
    runs the LangGraph pipeline, and returns an outfit recommendation.

    Errors:
        422 — location string could not be geocoded
        500 — unexpected pipeline failure
    """
    graph = build_graph()

    initial_state = {
        "session_id":  request.session_id,
        "location":    request.location,
        "description": request.message,  # renamed from description to match frontend
    }

    try:
        final_state = await graph.ainvoke(initial_state)
    except ValueError as exc:
        # Raised by get_geocode() when the location cannot be resolved
        raise HTTPException(status_code=422, detail=str(exc))
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Pipeline error: {exc}")

    return ChatResponse(
        session_id=     request.session_id,
        answer=         final_state["answer"],
        weather_summary=_format_weather_summary(final_state["weather"]),
        cache_hit=      final_state.get("cache_hit", False),
    )
