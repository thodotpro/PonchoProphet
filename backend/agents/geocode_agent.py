# backend/agents/geocode_agent.py
# Node 1: converts the raw location string in state to (lat, lon).

from graph.state import AgentState
from tools.get_geocode import get_geocode


def geocode_node(state: AgentState) -> dict:
    """
    Graph node — Geocoding.

    Reads:  state["location"]
    Writes: state["lat"], state["lon"]

    Raises ValueError (propagated to FastAPI as HTTP 422) if the location
    string cannot be resolved by the Open-Meteo geocoding API.
    """
    lat, lon = get_geocode(state["location"])
    return {"lat": lat, "lon": lon}
