from unittest.mock import AsyncMock, patch

import pytest

import agents.cache_agent
from agents.cache_agent import cache_node


WEATHER = {"temperature": 18.5, "weather_description": "Partly cloudy"}
STATE = {"session_id": "s1", "location": "Vienna", "lat": 48.21, "lon": 16.37}


async def test_cache_node_sets_cache_hit_and_weather_on_hit():
    with patch("agents.cache_agent.query_db", new_callable=AsyncMock, return_value=WEATHER):
        result = await cache_node(STATE)

    assert result["cache_hit"] is True
    assert result["weather"] == WEATHER


async def test_cache_node_sets_cache_miss_on_miss():
    with patch("agents.cache_agent.query_db", new_callable=AsyncMock, return_value=None):
        result = await cache_node(STATE)

    assert result["cache_hit"] is False
    assert "weather" not in result


