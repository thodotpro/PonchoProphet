# backend/agents/weather_agent.py
# Node 3: fetches fresh weather data from Open-Meteo and saves it to the cache.
# Only reached on a cache miss.

from graph.state import AgentState
from tools.call_weather_api import call_weather_api
from tools.save_db import save_db


def weather_node(state: AgentState) -> dict:
    """
    Graph node — Weather fetch (cache miss path).

    Reads:  state["lat"], state["lon"]
    Writes: state["weather"]

    Fetches from Open-Meteo, persists to SQLite so the next identical
    request within the TTL window will be served from cache.
    """
    weather = call_weather_api(state["lat"], state["lon"])
    save_db(state["lat"], state["lon"], weather)
    return {"weather": weather}
