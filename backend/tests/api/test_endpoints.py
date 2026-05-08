from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

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

PIPELINE_RESULT_MISS = {
    "answer": "Wear a raincoat.",
    "weather": WEATHER,
    "cache_hit": False,
}

PIPELINE_RESULT_HIT = {
    "answer": "Wear a raincoat.",
    "weather": WEATHER,
    "cache_hit": True,
}

VALID_PAYLOAD = {"session_id": "abc123", "location": "Vienna, Austria"}


# ---------------------------------------------------------------------------
# /health
# ---------------------------------------------------------------------------

def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# ---------------------------------------------------------------------------
# /chat — cache miss path
# ---------------------------------------------------------------------------

def test_chat_cache_miss_returns_200_with_chat_response():
    with patch("app.main._graph") as mock_graph:
        mock_graph.ainvoke = AsyncMock(return_value=PIPELINE_RESULT_MISS)
        response = client.post("/chat", json=VALID_PAYLOAD)

    assert response.status_code == 200
    body = response.json()
    assert body["session_id"] == "abc123"
    assert body["answer"] == "Wear a raincoat."
    assert body["cache_hit"] is False
    assert "weather_summary" in body


# ---------------------------------------------------------------------------
# /chat — cache hit path
# ---------------------------------------------------------------------------

def test_chat_cache_hit_returns_cache_hit_true():
    with patch("app.main._graph") as mock_graph:
        mock_graph.ainvoke = AsyncMock(return_value=PIPELINE_RESULT_HIT)
        response = client.post("/chat", json=VALID_PAYLOAD)

    assert response.status_code == 200
    assert response.json()["cache_hit"] is True


# ---------------------------------------------------------------------------
# /chat — error paths
# ---------------------------------------------------------------------------

def test_chat_unknown_location_returns_422():
    with patch("app.main._graph") as mock_graph:
        mock_graph.ainvoke = AsyncMock(side_effect=ValueError("Location not found: 'xyzzy'"))
        response = client.post("/chat", json={**VALID_PAYLOAD, "location": "xyzzy"})

    assert response.status_code == 422


def test_chat_weather_api_down_returns_503():
    with patch("app.main._graph") as mock_graph:
        mock_graph.ainvoke = AsyncMock(side_effect=ConnectionError("Connection refused"))
        response = client.post("/chat", json=VALID_PAYLOAD)

    assert response.status_code == 503


def test_chat_redis_down_still_returns_200():
    with patch("app.main._graph") as mock_graph:
        mock_graph.ainvoke = AsyncMock(return_value=PIPELINE_RESULT_MISS)
        response = client.post("/chat", json=VALID_PAYLOAD)

    assert response.status_code == 200
