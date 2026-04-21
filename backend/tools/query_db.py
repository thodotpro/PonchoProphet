# backend/tools/query_db.py
# Reads weather data from the SQLite cache, respecting the configured TTL.

import json
import os
import sqlite3
import time

from app.config import settings


def query_db(lat: float, lon: float) -> dict | None:
    """
    Look up cached weather data for the given (lat, lon).

    Returns:
        The weather dict if a fresh cache entry exists.
        None if there is no entry OR if the entry has expired (TTL exceeded).
    """
    if not os.path.exists(settings.sqlite_db_path):
        return None

    with sqlite3.connect(settings.sqlite_db_path) as conn:
        cursor = conn.execute(
            "SELECT weather, fetched_at FROM weather_cache WHERE lat = ? AND lon = ?",
            (lat, lon),
        )
        row = cursor.fetchone()

    if row is None:
        return None

    weather_json, fetched_at = row
    age_seconds = time.time() - fetched_at

    if age_seconds > settings.weather_cache_ttl_seconds:
        return None  # stale — caller will trigger a fresh fetch

    return json.loads(weather_json)
