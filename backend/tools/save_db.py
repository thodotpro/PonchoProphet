import json
import logging

from app.config import settings
from tools.redis_client import redis_client

logger = logging.getLogger(__name__)


async def save_db(lat: float, lon: float, weather: dict) -> None:
    """
    Upsert weather data for (lat, lon) into Redis.
    Errors are logged and swallowed — cache write failure must not abort the pipeline.
    """
    key = f"weather:{lat}:{lon}"
    try:
        await redis_client.setex(key, settings.weather_cache_ttl_seconds, json.dumps(weather))
    except Exception as exc:
        logger.warning("Redis write error for key %s: %s", key, exc)
