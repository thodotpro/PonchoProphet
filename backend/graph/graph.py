# backend/graph/graph.py
# Assembles all nodes into the compiled LangGraph pipeline.
# This is the only file that knows how the nodes connect — all other files
# are unaware of the graph topology.

from langgraph.graph import StateGraph, END

from agents.cache_agent import cache_node
from agents.geocode_agent import geocode_node
from agents.outfit_agent import outfit_node
from agents.weather_agent import weather_node
from graph.state import AgentState


def _route_after_cache(state: AgentState) -> str:
    """
    Conditional routing function called after cache_node.

    Returns the name of the next node to execute:
    - "outfit_node"  → cache hit, weather is already in state
    - "weather_node" → cache miss, need to fetch from Open-Meteo
    """
    return "outfit_node" if state.get("cache_hit") else "weather_node"


def build_graph():
    """
    Build and compile the PonchoProphet deterministic pipeline.

    Graph topology:
        geocode_node → cache_node → (cache hit?)  → outfit_node → END
                                  → (cache miss?) → weather_node → outfit_node → END

    No checkpointer: each request is fully independent (single-shot).
    """
    g = StateGraph(AgentState)

    # Register nodes
    g.add_node("geocode_node", geocode_node)
    g.add_node("cache_node",   cache_node)
    g.add_node("weather_node", weather_node)
    g.add_node("outfit_node",  outfit_node)

    # Entry point
    g.set_entry_point("geocode_node")

    # Deterministic edges
    g.add_edge("geocode_node", "cache_node")

    # Conditional edge: cache hit → outfit, cache miss → weather → outfit
    g.add_conditional_edges(
        "cache_node",
        _route_after_cache,
        {
            "outfit_node":  "outfit_node",
            "weather_node": "weather_node",
        },
    )

    g.add_edge("weather_node", "outfit_node")
    g.add_edge("outfit_node",  END)

    return g.compile()  # no checkpointer — single-shot requests
