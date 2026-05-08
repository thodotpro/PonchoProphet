# [ISSUE-03] Async HTTP tool layer

**Labels:** needs-triage  
**Type:** AFK

## What to build

Convert all outbound HTTP calls to `httpx.AsyncClient` so geocoding, weather fetching, and Ollama liveness checks are non-blocking. Make the corresponding graph nodes `async def`. Classify errors correctly: unresolvable location → `ValueError` (surfaces as HTTP 422); network failure → HTTP 503 with a user-facing message. Include tests for each tool and node.

Demoable by: submitting an unknown location and receiving a 422 (not a 500); simulating a network timeout and receiving a 503.

## Acceptance criteria

- [ ] `get_geocode` uses `httpx.AsyncClient` and is `async def`
- [ ] `call_weather_api` uses `httpx.AsyncClient` and is `async def`
- [ ] `is_ollama_online` in `llm_factory` uses `httpx.AsyncClient` and is `async def`
- [ ] `geocode_node` is `async def`
- [ ] `weather_node` is `async def`
- [ ] Unresolvable location raises `ValueError` → FastAPI returns HTTP 422
- [ ] Network error in geocoding or weather fetch → FastAPI returns HTTP 503 with user-facing message (not a raw 500)
- [ ] Unit test: `get_geocode` returns `(lat, lon)` for valid location
- [ ] Unit test: `get_geocode` raises `ValueError` for unknown location
- [ ] Unit test: `get_geocode` raises network error type on connection failure
- [ ] Unit test: `call_weather_api` returns expected weather dict shape for valid coordinates
- [ ] Unit test: `call_weather_api` raises on connection failure
- [ ] Unit test: `geocode_node` writes `lat` and `lon` to state
- [ ] Unit test: `weather_node` writes `weather` to state

## Blocked by

None — can start immediately.
