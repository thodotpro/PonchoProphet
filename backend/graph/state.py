from typing import TypedDict, NotRequired


class AgentState(TypedDict):
    session_id:   str
    location:     str                # raw string from user e.g. "Vienna, Austria"
    description:  NotRequired[str]   # optional: user style / self-description
    lat:          NotRequired[float] # set by geocode_node
    lon:          NotRequired[float] # set by geocode_node
    weather:      NotRequired[dict]  # set by cache_node (hit) or weather_node (miss)
    cache_hit:    NotRequired[bool]  # set by cache_node
    answer:       NotRequired[str]   # set by outfit_node
