import json
import logging

from tools.redis_client import redis_client

logger = logging.getLogger(__name__)


async def query_db(lat: float, lon: float) -> dict | None:
    """
    Look up cached weather data for the given (lat, lon).

    Returns the weather dict on hit, None on miss or Redis error.
    Redis errors are logged and treated as cache misses so the pipeline continues.
    """
    key = f"weather:{lat}:{lon}"
    try:
        data = await redis_client.get(key)
    except Exception as exc:
        logger.warning("Redis read error for key %s: %s", key, exc)
        return None

    if data:
        return json.loads(data)
    return None
