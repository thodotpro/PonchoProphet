# [ISSUE-05] Full API endpoint test suite

**Labels:** needs-triage  
**Type:** AFK

## What to build

Add `TestClient` tests covering the full `/chat` and `/health` endpoints with all external IO mocked. Validate both the cache-hit path and the cache-miss path through the pipeline. Confirm correct HTTP status codes for error scenarios.

Demoable by: running `pytest` and seeing the full suite pass with no live network calls.

## Acceptance criteria

- [ ] `GET /health` returns `{"status": "ok"}` with HTTP 200
- [ ] `POST /chat` with valid payload and cache miss returns HTTP 200 with correct `ChatResponse` shape (`session_id`, `answer`, `weather_summary`, `cache_hit=False`)
- [ ] `POST /chat` with valid payload and cache hit returns HTTP 200 with `cache_hit=True` and no weather API call made
- [ ] `POST /chat` with unresolvable location returns HTTP 422
- [ ] `POST /chat` when weather API is unreachable returns HTTP 503
- [ ] `POST /chat` with Redis down still returns HTTP 200 (cache-miss path, graceful degradation)
- [ ] All tests use mocked IO — no live network calls or real Redis connection required
- [ ] `pytest` runs the full suite without environment variables set

## Blocked by

- ISSUE-02 (async Redis + graceful degradation must be in place)
- ISSUE-03 (async HTTP + error classification must be in place)
- ISSUE-04 (graph singleton + async LLM must be in place)
