# backend/tools/query_db.py
# Reads weather data from the Redis cache.

import json
from tools.redis_client import redis_client


def query_db(lat: float, lon: float) -> dict | None:
    """
    Look up cached weather data for the given (lat, lon).

    Returns:
        The weather dict if a fresh cache entry exists.
        None if there is no entry or if it has expired.
    """
    key = f"weather:{lat}:{lon}"
    data = redis_client.get(key)
    
    if data:
        return json.loads(data)
    
    return None
