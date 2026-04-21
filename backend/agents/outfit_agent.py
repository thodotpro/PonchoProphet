# backend/agents/outfit_agent.py
# Node 4: the only LLM-powered node. Calls Claude to generate an outfit
# recommendation based on the current weather and optional user description.

from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage

from app.config import settings
from graph.state import AgentState

SYSTEM_PROMPT = (
    "You are PonchoProphet, a witty and practical outfit advisor. "
    "Based on the current weather conditions — and optionally the user's personal "
    "style or self-description — give a concise, friendly outfit recommendation. "
    "Be specific about clothing items (jacket type, layers, umbrella, sunscreen, etc.). "
    "Keep the response to 3–5 sentences. Natural, conversational tone — no bullet points."
)


def _build_user_message(state: AgentState) -> str:
    """Compose the user-facing prompt from weather data and optional description."""
    w = state["weather"]

    weather_block = (
        f"Current weather conditions:\n"
        f"- Temperature: {w['temperature']}{w['unit_temperature']} "
        f"(feels like {w['apparent_temperature']}{w['unit_temperature']})\n"
        f"- Conditions: {w['weather_description']}\n"
        f"- Precipitation probability: {w['precipitation_probability']}%\n"
        f"- Precipitation: {w['precipitation']} mm\n"
        f"- Wind speed: {w['windspeed']} {w['unit_windspeed']}\n"
        f"- UV index: {w['uv_index']}\n"
    )

    description_block = ""
    if state.get("description"):
        description_block = (
            f"\nUser's style / self-description:\n{state['description']}\n"
        )

    return f"{weather_block}{description_block}\nWhat should I wear today?"


def outfit_node(state: AgentState) -> dict:
    """
    Graph node — Outfit recommendation (LLM).

    Reads:  state["weather"], state["description"] (optional)
    Writes: state["answer"]

    Instantiates ChatAnthropic per-request so the model/key can be changed
    via environment variables without restarting the server.
    """
    llm = ChatAnthropic(
        model=settings.anthropic_model,
        api_key=settings.anthropic_api_key,
        max_tokens=512,
    )

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=_build_user_message(state)),
    ]

    response = llm.invoke(messages)
    return {"answer": response.content}
