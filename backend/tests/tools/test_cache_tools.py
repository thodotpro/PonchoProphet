import json
from unittest.mock import AsyncMock, patch

import pytest

import tools.query_db
import tools.save_db
from tools.query_db import query_db
from tools.save_db import save_db


WEATHER = {
    "temperature": 18.5,
    "apparent_temperature": 16.0,
    "precipitation_probability": 20,
    "precipitation": 0.0,
    "weathercode": 2,
    "weather_description": "Partly cloudy",
    "windspeed": 12.3,
    "uv_index": 4,
    "unit_temperature": "°C",
    "unit_windspeed": "km/h",
}


# ---------------------------------------------------------------------------
# query_db
# ---------------------------------------------------------------------------

async def test_query_db_returns_weather_on_cache_hit():
    mock_client = AsyncMock()
    mock_client.get = AsyncMock(return_value=json.dumps(WEATHER))

    with patch("tools.query_db.redis_client", mock_client):
        result = await query_db(48.21, 16.37)

    assert result == WEATHER


async def test_query_db_returns_none_on_cache_miss():
    mock_client = AsyncMock()
    mock_client.get = AsyncMock(return_value=None)

    with patch("tools.query_db.redis_client", mock_client):
        result = await query_db(48.21, 16.37)

    assert result is None


async def test_query_db_returns_none_on_redis_error():
    mock_client = AsyncMock()
    mock_client.get = AsyncMock(side_effect=ConnectionError("Redis down"))

    with patch("tools.query_db.redis_client", mock_client):
        result = await query_db(48.21, 16.37)

    assert result is None


# ---------------------------------------------------------------------------
# save_db
# ---------------------------------------------------------------------------

async def test_save_db_does_not_raise_on_redis_error():
    mock_client = AsyncMock()
    mock_client.setex = AsyncMock(side_effect=ConnectionError("Redis down"))

    with patch("tools.save_db.redis_client", mock_client):
        await save_db(48.21, 16.37, WEATHER)  # must not raise
