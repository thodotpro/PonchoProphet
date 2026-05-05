from graph.state import AgentState
from tools.call_weather_api import call_weather_api
from tools.save_db import save_db


async def weather_node(state: AgentState) -> dict:
    """
    Graph node — Weather fetch (cache miss path).

    Reads:  state["lat"], state["lon"]
    Writes: state["weather"]
    """
    weather = await call_weather_api(state["lat"], state["lon"])
    await save_db(state["lat"], state["lon"], weather)
    return {"weather": weather}
