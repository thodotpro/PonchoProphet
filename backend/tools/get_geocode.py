import httpx

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"


async def get_geocode(location: str) -> tuple[float, float]:
    """
    Convert a location string to (lat, lon) rounded to 2 decimal places.

    2 decimal places ≈ 1 km precision — avoids cache misses from trivial differences.

    Raises:
        ValueError: if the location cannot be resolved.
        httpx.HTTPError: on network or API errors.
    """
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(
            GEOCODING_URL,
            params={"name": location, "count": 1, "language": "en", "format": "json"},
        )
        response.raise_for_status()
        data = response.json()

    results = data.get("results")
    if not results:
        raise ValueError(f"Location not found: {location!r}")

    lat = round(results[0]["latitude"], 2)
    lon = round(results[0]["longitude"], 2)
    return lat, lon
