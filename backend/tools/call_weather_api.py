import httpx

WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

HOURLY_VARS = [
    "temperature_2m",
    "apparent_temperature",
    "precipitation_probability",
    "precipitation",
    "weathercode",
    "windspeed_10m",
    "uv_index",
]

WMO_CODES: dict[int, str] = {
    0:  "Clear sky",
    1:  "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Foggy",        48: "Depositing rime fog",
    51: "Light drizzle",   53: "Moderate drizzle",   55: "Dense drizzle",
    61: "Slight rain",     63: "Moderate rain",       65: "Heavy rain",
    71: "Slight snow",     73: "Moderate snow",       75: "Heavy snow",
    77: "Snow grains",
    80: "Slight rain showers", 81: "Moderate rain showers", 82: "Violent rain showers",
    85: "Slight snow showers", 86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail", 99: "Thunderstorm with heavy hail",
}


async def call_weather_api(lat: float, lon: float) -> dict:
    """
    Fetch current weather from Open-Meteo for the given coordinates.

    Raises:
        httpx.HTTPError: on network or API errors.
    """
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(
            WEATHER_URL,
            params={
                "latitude":        lat,
                "longitude":       lon,
                "hourly":          ",".join(HOURLY_VARS),
                "current_weather": "true",
                "forecast_days":   1,
                "timezone":        "auto",
            },
        )
        response.raise_for_status()
        data = response.json()

    current_time = data["current_weather"]["time"]
    hourly_times = data["hourly"]["time"]
    try:
        idx = hourly_times.index(current_time)
    except ValueError:
        idx = 0

    h = data["hourly"]
    units = data["hourly_units"]
    weathercode = h["weathercode"][idx]

    return {
        "temperature":               round(h["temperature_2m"][idx], 1),
        "apparent_temperature":      round(h["apparent_temperature"][idx], 1),
        "precipitation_probability": h["precipitation_probability"][idx],
        "precipitation":             h["precipitation"][idx],
        "weathercode":               weathercode,
        "weather_description":       WMO_CODES.get(weathercode, "Unknown"),
        "windspeed":                 round(h["windspeed_10m"][idx], 1),
        "uv_index":                  h["uv_index"][idx],
        "unit_temperature":          units["temperature_2m"],
        "unit_windspeed":            units["windspeed_10m"],
    }
