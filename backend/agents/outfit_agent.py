from agents.llm_factory import get_llm
from langchain_core.messages import HumanMessage, SystemMessage

from graph.state import AgentState

SYSTEM_PROMPT = (
    "You are PonchoProphet, a witty and practical outfit advisor. "
    "Based on the current weather conditions — and optionally the user's personal "
    "style or self-description — give a concise, friendly outfit recommendation. "
    "Be specific about clothing items (jacket type, layers, umbrella, sunscreen, etc.). "
    "Keep the response to 3–5 sentences. Natural, conversational tone — no bullet points."
)


def _build_user_message(state: AgentState) -> str:
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
        description_block = f"\nUser's style / self-description:\n{state['description']}\n"

    return f"{weather_block}{description_block}\nWhat should I wear today?"


async def outfit_node(state: AgentState) -> dict:
    """
    Graph node — Outfit recommendation (LLM).

    Reads:  state["weather"], state["description"] (optional)
    Writes: state["answer"]
    """
    llm = await get_llm()
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=_build_user_message(state)),
    ]
    response = await llm.ainvoke(messages)
    return {"answer": response.content}
