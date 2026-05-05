# PRD: Backend Reliability & Production Hardening

**Status:** needs-triage  
**Area:** backend  

---

## Problem Statement

PonchoProphet's backend is functionally correct in single-request development scenarios, but has several structural issues that will cause degraded performance, request failures, and unpredictable errors under real production load.

The core problem: the backend is built with a sync-first mental model inside an async FastAPI application. Every request blocks the event loop during geocoding, weather fetching, Redis lookups, and LLM calls. Additionally, the LangGraph pipeline is compiled fresh on every request, Redis connectivity failures crash requests instead of degrading gracefully, and test coverage is near-zero — making it impossible to validate fixes or catch regressions safely.

Users experience this as: slow responses under concurrent load, intermittent 500 errors when Redis is momentarily unavailable, and no confidence that changes to the pipeline won't silently break something.

---

## Solution

Harden the backend for production by making all IO non-blocking, compiling the graph once at startup, degrading gracefully on Redis failure, and establishing a test suite that validates the pipeline's external behavior.

---

## User Stories

1. As a user submitting an outfit request, I want the server to respond quickly even when other users are making requests simultaneously, so that the app feels responsive at all times.
2. As a user, I want to receive an outfit recommendation even if the Redis cache is temporarily unavailable, so that a cache outage doesn't fully block me.
3. As a user, I want a clear error message when my location cannot be found, rather than a generic 500, so that I know what went wrong.
4. As a user, I want a clear error message when weather data cannot be fetched due to a network issue, so that I understand the failure.
5. As a user, I want consistent response times regardless of whether my result is served from cache or fetched live, so that the app feels predictable.
6. As a developer, I want the backend to use the most current Anthropic model available, so that recommendations benefit from the latest capabilities.
7. As a developer, I want dependency versions pinned so that CI deployments are reproducible and don't break silently on upstream releases.
8. As a developer, I want all IO operations to be non-blocking, so that the FastAPI event loop is never stalled by a network call.
9. As a developer, I want the LangGraph pipeline compiled once at startup rather than per-request, so that latency is not wasted on graph compilation overhead.
10. As a developer, I want integration tests for each graph node and tool, so that I can make changes with confidence and catch regressions immediately.
11. As a developer, I want integration tests for the `/chat` endpoint, so that I can validate the full request/response contract without a live LLM or external APIs.
12. As a developer, I want tests for the cache hit and cache miss routing paths, so that I can confirm the LangGraph conditional edge behaves correctly.
13. As a developer, I want to know which LLM provider handled a request (via logging), so that I can diagnose provider-selection issues in production.
14. As a developer deploying to Render, I want CORS locked to specific methods and headers rather than `*`, so that the API surface is not unnecessarily broad.
15. As a developer, I want Redis connection errors to be caught and logged, so that cache failures produce a warning rather than an unhandled 500.
16. As an operator, I want the lifespan hook to validate required configuration at startup, so that misconfigured deployments fail fast with a clear message rather than erroring at request time.

---

## Implementation Decisions

### Async IO throughout

All network IO must be made non-blocking:

- Replace all `httpx.Client` (sync) usages in the geocoding and weather tools with `httpx.AsyncClient` and `await`.
- Replace the synchronous Redis client with `redis.asyncio` (`aioredis`-compatible interface shipped with the `redis` package).
- Replace synchronous `llm.invoke()` in the outfit node with `await llm.ainvoke()`.
- The Ollama liveness check in the LLM factory (`httpx.get`) must also become async.

All graph nodes that perform IO must be declared `async def` so LangGraph can `await` them properly.

### Graph singleton

`build_graph()` must be called once at module level (or inside the FastAPI lifespan hook) and reused across all requests. The compiled graph object is stateless and safe to share across concurrent invocations — LangGraph passes a fresh state dict per `ainvoke` call.

### Graceful Redis degradation

The cache lookup tool must catch Redis connectivity errors and return `None` (treating the result as a cache miss) rather than raising. The cache write tool must catch and log errors without interrupting the pipeline. The pipeline must remain functional with Redis fully offline — it will simply always miss the cache.

### Error classification in tools

- Geocoding failure (location not found): raise `ValueError` → surfaces as HTTP 422.
- Network failure in geocoding or weather fetch: raise a distinct error type → surfaces as HTTP 503 with a user-friendly message, not a 500.
- LLM provider unavailable: `ValueError` from factory → surfaces as HTTP 503.

### LLM factory logging

When `get_llm()` selects a provider, it should log which provider and model was chosen at INFO level. This aids production diagnostics without adding complexity.

### Model version

The default Anthropic model in config should be updated to `claude-haiku-4-5-20251001` (current Haiku 4.5).

### CORS scope

`allow_methods` should be locked to `["GET", "POST"]`. `allow_headers` should be locked to `["Content-Type"]`. The wildcard values are unnecessarily broad.

### Dependency pinning

All LangGraph ecosystem packages (`langgraph`, `langchain-core`, `langchain-anthropic`, `langchain-openai`, `langchain-ollama`) must be pinned to specific versions. Add `pytest-asyncio` and `httpx` (already present but confirm) to the test dependencies.

### Startup validation (lifespan hook)

The existing empty lifespan hook should validate that at least one LLM provider is reachable or configured. If none is available at startup, log a warning (not a hard failure — Ollama may come online later).

---

## Testing Decisions

### What makes a good test

Tests should exercise external behavior — what goes in, what comes out, what errors are raised — not internal implementation details like which Redis method was called. Prefer testing at the tool and node boundary, not at the line level.

### Modules to test

**Tools (unit-level, all IO mocked):**
- Geocoding tool: valid location returns `(lat, lon)`; unknown location raises `ValueError`; network error raises appropriate error.
- Weather tool: valid coordinates return expected weather dict shape; network error raises.
- Cache query tool: Redis hit returns dict; Redis miss returns `None`; Redis error returns `None` (graceful degradation).
- Cache save tool: Redis error is caught and logged, does not raise.

**LLM Factory (unit-level, already partially covered):**
- Existing `test_llm_factory.py` covers the four provider-selection paths. Add: test that selected provider is logged.

**Graph nodes (integration-level, external APIs mocked):**
- `geocode_node`: maps state `location` → `lat`, `lon`.
- `cache_node`: returns `cache_hit=True` + `weather` on hit; `cache_hit=False` on miss; `cache_hit=False` on Redis error.
- `weather_node`: returns `weather` dict on success.
- `outfit_node`: returns non-empty `answer` string.

**Full pipeline (integration-level, all external IO mocked):**
- Cache hit path: `geocode → cache(hit) → outfit` — weather not fetched.
- Cache miss path: `geocode → cache(miss) → weather → outfit` — full pipeline.

**API endpoint (FastAPI TestClient):**
- `POST /chat` with valid payload returns 200 with expected `ChatResponse` shape.
- `POST /chat` with unresolvable location returns 422.
- `GET /health` returns 200.

### Prior art

There is one existing test file (`tests/agents/test_llm_factory.py`) using `pytest` with `unittest.mock.patch`. New tests should follow the same style: `pytest` fixtures, `patch` for external IO, assert on return values and raised exceptions.

---

## Out of Scope

- Streaming LLM responses to the frontend (chunked SSE).
- Multi-turn conversation history / LangGraph checkpointing.
- Authentication or per-user rate limiting.
- Monitoring integration (Sentry, Datadog) — noted in `todo.md` as a separate initiative.
- Frontend changes — addressed in a separate `todo.md` item.
- CI/CD pipeline (GitHub Actions → Render) — separate `todo.md` item.
- Switching the LLM provider priority order (Ollama → OpenAI → Anthropic is intentional for local dev).

---

## Further Notes

- The backend targets Render for hosting (single-process, `gunicorn` with `UvicornWorker`). Async correctness is especially important since a blocked event loop under Gunicorn kills throughput for all concurrent requests on that worker.
- Redis is a soft dependency — the pipeline must degrade gracefully without it. The cache is a performance optimisation, not a required data store.
- The `AgentState` TypedDict is the single source of truth for what each node reads and writes. Any new fields added during this work must be reflected there.
- `schemas.py` is the API contract shared with the frontend. No changes to `ChatRequest` or `ChatResponse` are needed for this work.
