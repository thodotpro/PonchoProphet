# backend/app/graph/checkpointer.py
# Dev B owns this file.
# It connects LangGraph's memory system to Redis.

import os
from langgraph.checkpoint.redis import RedisSaver

def get_checkpointer():
    """
    Returns a LangGraph checkpointer backed by Redis.
    
    A checkpointer is what gives LangGraph "memory" between graph runs.
    Without it, every call to graph.invoke() starts from a blank state.
    With it, LangGraph stores and reloads state keyed on session_id —
    so the second message in a conversation picks up where the first left off.
    
    🎓 LEARNING COMPLEXITY: This is the "persistence" in "persistent agents".
    The checkpointer is also what enables time-travel debugging —
    you can replay a graph from any previous checkpoint.
    
    For learning, swap this to MemorySaver() (in-process, no Redis)
    and the rest of the code works identically — just without durability.
    """
    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
    return RedisSaver.from_conn_string(redis_url)