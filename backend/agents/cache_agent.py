# backend/agents/cache_agent.py
# Node 2: checks the SQLite cache for existing weather data.

from graph.state import AgentState
from tools.query_db import query_db


def cache_node(state: AgentState) -> dict:
    """
    Graph node — Cache lookup.

    Reads:  state["lat"], state["lon"]
    Writes: state["weather"] + state["cache_hit"] = True  (on hit)
            state["cache_hit"] = False                     (on miss)

    The conditional edge in graph.py reads cache_hit to decide whether
    to skip to outfit_node (hit) or pass through weather_node (miss).
    """
    result = query_db(state["lat"], state["lon"])

    if result is not None:
        return {"weather": result, "cache_hit": True}

    return {"cache_hit": False}
