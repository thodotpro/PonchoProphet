from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

import tools.get_geocode
import tools.call_weather_api
from tools.get_geocode import get_geocode
from tools.call_weather_api import call_weather_api


def _make_response(status_code: int, json_data: dict) -> MagicMock:
    resp = MagicMock(spec=httpx.Response)
    resp.status_code = status_code
    resp.json.return_value = json_data
    resp.raise_for_status = MagicMock()
    return resp


# ---------------------------------------------------------------------------
# get_geocode
# ---------------------------------------------------------------------------

GEOCODE_RESPONSE = {
    "results": [{"latitude": 48.2093, "longitude": 16.3728, "name": "Vienna"}]
}


async def test_get_geocode_returns_lat_lon_for_valid_location():
    resp = _make_response(200, GEOCODE_RESPONSE)
    mock_client = AsyncMock()
    mock_client.__aenter__ = AsyncMock(return_value=mock_client)
    mock_client.__aexit__ = AsyncMock(return_value=False)
    mock_client.get = AsyncMock(return_value=resp)

    with patch("tools.get_geocode.httpx.AsyncClient", return_value=mock_client):
        lat, lon = await get_geocode("Vienna, Austria")

    assert lat == round(48.2093, 2)
    assert lon == round(16.3728, 2)


async def test_get_geocode_raises_value_error_for_unknown_location():
    resp = _make_response(200, {"results": []})
    mock_client = AsyncMock()
    mock_client.__aenter__ = AsyncMock(return_value=mock_client)
    mock_client.__aexit__ = AsyncMock(return_value=False)
    mock_client.get = AsyncMock(return_value=resp)

    with patch("tools.get_geocode.httpx.AsyncClient", return_value=mock_client):
        with pytest.raises(ValueError, match="Location not found"):
            await get_geocode("xyzzy_nonexistent_place")


async def test_get_geocode_raises_on_network_failure():
    mock_client = AsyncMock()
    mock_client.__aenter__ = AsyncMock(return_value=mock_client)
    mock_client.__aexit__ = AsyncMock(return_value=False)
    mock_client.get = AsyncMock(side_effect=httpx.ConnectError("timeout"))

    with patch("tools.get_geocode.httpx.AsyncClient", return_value=mock_client):
        with pytest.raises(httpx.ConnectError):
            await get_geocode("Vienna, Austria")


# ---------------------------------------------------------------------------
# call_weather_api
# ---------------------------------------------------------------------------

WEATHER_RESPONSE = {
    "current_weather": {"time": "2024-01-15T14:00"},
    "hourly": {
        "time": ["2024-01-15T14:00"],
        "temperature_2m": [12.5],
        "apparent_temperature": [10.0],
        "precipitation_probability": [30],
        "precipitation": [0.2],
        "weathercode": [61],
        "windspeed_10m": [15.0],
        "uv_index": [2],
    },
    "hourly_units": {
        "temperature_2m": "°C",
        "windspeed_10m": "km/h",
    },
}


async def test_call_weather_api_returns_weather_dict():
    resp = _make_response(200, WEATHER_RESPONSE)
    mock_client = AsyncMock()
    mock_client.__aenter__ = AsyncMock(return_value=mock_client)
    mock_client.__aexit__ = AsyncMock(return_value=False)
    mock_client.get = AsyncMock(return_value=resp)

    with patch("tools.call_weather_api.httpx.AsyncClient", return_value=mock_client):
        result = await call_weather_api(48.21, 16.37)

    assert result["temperature"] == 12.5
    assert result["weather_description"] == "Slight rain"
    assert result["unit_temperature"] == "°C"


async def test_call_weather_api_raises_on_network_failure():
    mock_client = AsyncMock()
    mock_client.__aenter__ = AsyncMock(return_value=mock_client)
    mock_client.__aexit__ = AsyncMock(return_value=False)
    mock_client.get = AsyncMock(side_effect=httpx.ConnectError("timeout"))

    with patch("tools.call_weather_api.httpx.AsyncClient", return_value=mock_client):
        with pytest.raises(httpx.ConnectError):
            await call_weather_api(48.21, 16.37)
