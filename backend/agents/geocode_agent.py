from graph.state import AgentState
from tools.get_geocode import get_geocode


async def geocode_node(state: AgentState) -> dict:
    """
    Graph node — Geocoding.

    Reads:  state["location"]
    Writes: state["lat"], state["lon"]

    Raises ValueError (-> HTTP 422) if location cannot be resolved.
    """
    lat, lon = await get_geocode(state["location"])
    return {"lat": lat, "lon": lon}
