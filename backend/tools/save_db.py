# backend/tools/save_db.py
# Writes weather data to the SQLite cache.

import json
import sqlite3
import time

from app.config import settings


def init_db() -> None:
    """
    Create the weather_cache table if it doesn't already exist.
    Called once at application startup via the FastAPI lifespan hook.
    """
    with sqlite3.connect(settings.sqlite_db_path) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS weather_cache (
                lat        REAL    NOT NULL,
                lon        REAL    NOT NULL,
                weather    TEXT    NOT NULL,   -- JSON blob
                fetched_at REAL    NOT NULL,   -- Unix timestamp (time.time())
                PRIMARY KEY (lat, lon)
            )
        """)
        conn.commit()


def save_db(lat: float, lon: float, weather: dict) -> None:
    """
    Upsert weather data for the given (lat, lon) into the SQLite cache.

    Uses INSERT OR REPLACE so re-fetching the same location simply
    overwrites the old row and resets the TTL clock.
    """
    with sqlite3.connect(settings.sqlite_db_path) as conn:
        conn.execute(
            """
            INSERT OR REPLACE INTO weather_cache (lat, lon, weather, fetched_at)
            VALUES (?, ?, ?, ?)
            """,
            (lat, lon, json.dumps(weather), time.time()),
        )
        conn.commit()
