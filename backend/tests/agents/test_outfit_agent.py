from unittest.mock import AsyncMock, patch

import pytest

import agents.outfit_agent
from agents.outfit_agent import outfit_node


WEATHER = {
    "temperature": 12.5,
    "apparent_temperature": 10.0,
    "precipitation_probability": 30,
    "precipitation": 0.2,
    "weathercode": 61,
    "weather_description": "Slight rain",
    "windspeed": 15.0,
    "uv_index": 2,
    "unit_temperature": "°C",
    "unit_windspeed": "km/h",
}

STATE = {"session_id": "s1", "location": "Vienna", "lat": 48.21, "lon": 16.37, "weather": WEATHER}


async def test_outfit_node_returns_non_empty_answer():
    mock_llm = AsyncMock()
    mock_llm.ainvoke = AsyncMock(return_value=AsyncMock(content="Wear a raincoat today."))

    with patch("agents.outfit_agent.get_llm", new_callable=AsyncMock, return_value=mock_llm):
        result = await outfit_node(STATE)

    assert "answer" in result
    assert len(result["answer"]) > 0


async def test_outfit_node_includes_description_when_provided():
    state_with_desc = {**STATE, "description": "I prefer casual clothing"}
    mock_llm = AsyncMock()
    mock_llm.ainvoke = AsyncMock(return_value=AsyncMock(content="Casual raincoat works great."))

    with patch("agents.outfit_agent.get_llm", new_callable=AsyncMock, return_value=mock_llm):
        result = await outfit_node(state_with_desc)

    assert len(result["answer"]) > 0
