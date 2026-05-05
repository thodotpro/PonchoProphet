from graph.state import AgentState
from tools.query_db import query_db


async def cache_node(state: AgentState) -> dict:
    """
    Graph node — Cache lookup.

    Reads:  state["lat"], state["lon"]
    Writes: state["weather"] + state["cache_hit"] = True  (on hit)
            state["cache_hit"] = False                     (on miss or Redis error)
    """
    result = await query_db(state["lat"], state["lon"])

    if result is not None:
        return {"weather": result, "cache_hit": True}

    return {"cache_hit": False}
