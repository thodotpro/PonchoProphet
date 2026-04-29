# backend/tools/save_db.py
# Writes weather data to the Redis cache.

import json
from app.config import settings
from tools.redis_client import redis_client


def save_db(lat: float, lon: float, weather: dict) -> None:
    """
    Upsert weather data for the given (lat, lon) into the Redis cache.
    Uses lat:lon as the key and sets a TTL.
    """
    key = f"weather:{lat}:{lon}"
    redis_client.setex(
        key,
        settings.weather_cache_ttl_seconds,
        json.dumps(weather)
    )
