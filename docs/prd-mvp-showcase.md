# PRD: Poncho Prophet — MVP Showcase

## Problem Statement

Poncho Prophet has a working backend pipeline (LangGraph + Ollama + Redis + Open-Meteo) and a Vue frontend, but the two are not connected — the frontend still serves mocked responses. There is no one-command way to run the full stack, making it impossible to demonstrate the app end-to-end to a university audience.

## Solution

Wire the frontend to the backend, add a style preference input so the LLM can tailor recommendations, and package everything with Docker Compose so the showcase runs with a single command. Ollama runs on the host (not in Docker) so it has full CPU access and pre-pulled models.

## User Stories

1. As a showcase visitor, I want to type my city and hit Send, so that I receive a personalised outfit recommendation without any setup on my part.
2. As a showcase visitor, I want to describe my personal style (e.g. "I prefer smart-casual, love layers"), so that the recommendation reflects my wardrobe preferences.
3. As a showcase visitor, I want to see the current weather summary (temperature, conditions, rain probability) alongside the outfit suggestion, so that I understand why the recommendation was made.
4. As a showcase visitor, I want to see a "cached" badge on repeat queries for the same location, so that the Redis caching feature is visibly demonstrated.
5. As a showcase visitor, I want the app to respond quickly on a second request for the same location, so that the cache benefit is obvious.
6. As a showcase visitor, I want a typing indicator while the LLM is thinking, so that the app feels responsive rather than frozen.
7. As a showcase visitor, I want the app to work even if the local Ollama instance is unavailable, so that the demo does not break if the presenter forgot to start Ollama (falls back to cloud LLM).
8. As a presenter, I want to start the full stack with `docker-compose up`, so that I do not need to explain multi-step setup to the audience.
9. As a presenter, I want an `.env.example` file documenting every environment variable, so that I or a teammate can configure the stack without reading source code.
10. As a presenter, I want the Ollama model to default to `gemma4:e2b`, so that the demo uses the intended edge-optimised reasoning model.
11. As a developer, I want the Vite dev server to proxy `/api` requests to the FastAPI backend, so that I can develop frontend and backend independently without CORS issues.
12. As a developer, I want the backend container to reach the host Ollama service via `host.docker.internal`, so that the app works on Linux, Mac, and Windows without manual IP configuration.
13. As a developer, I want Redis to be a required service in Docker Compose, so that the caching feature is always active during the showcase.
14. As a developer, I want the LLM fallback chain (Ollama → OpenAI → Anthropic) to remain intact, so that any team member can run the stack with whichever credentials they have.

## Implementation Decisions

### Modules to build or modify

**Config module**
- Update `ollama_model` default from `gemma2:2b` to `gemma4:e2b`.
- Update `allowed_origins` default to `*` (tighten post-MVP).
- No interface changes — values still read from environment variables or `.env`.

**API schema**
- The existing `message` field on `ChatRequest` is already an optional free-text field that the outfit agent uses as a style/self-description hint. No schema changes required.
- The frontend label/placeholder will be updated to invite style descriptions (e.g. "Describe your style — casual, layered, colourful…").

**Outfit agent**
- No structural changes. The `description` field from state already flows into the LLM prompt as "User's style / self-description". The existing prompt handles it correctly.
- If the style input is empty, the agent already falls back gracefully.

**Frontend Chat component**
- Remove the fake/mocked response block.
- Uncomment and activate the real `fetch('/api/chat', ...)` call.
- Rename/re-hint the message input to clearly invite style descriptions.
- Ensure error states (network failure, 422, 503) surface clearly in the chat.

**Vite config**
- Add `server.proxy` so that `/api` requests in development are forwarded to `http://localhost:8000`.
- No changes needed for production (Nginx handles proxying).

**Docker Compose**
- Three services: `redis`, `backend`, `frontend`.
- `redis`: official `redis:7-alpine` image, no persistence needed for MVP.
- `backend`: built from `backend/Dockerfile`. Environment variables inject `REDIS_URL=redis://redis:6379/0`, `OLLAMA_BASE_URL=http://host.docker.internal:11434`, `OLLAMA_MODEL=gemma4:e2b`, `ALLOWED_ORIGINS=*`. Add `extra_hosts: ["host.docker.internal:host-gateway"]` for Linux compatibility.
- `frontend`: multi-stage build — Vite build stage, then Nginx alpine serving the `dist/` output. Nginx proxies `/api/` to the backend service.

**Nginx config**
- Serve the Vue SPA at `/`.
- Proxy `/api/` to `http://backend:8000/`.
- Handle SPA routing: all unmatched paths return `index.html` (so Vue Router works).

**`.env.example`**
- Document: `OLLAMA_MODEL`, `OLLAMA_BASE_URL`, `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `REDIS_URL`, `ALLOWED_ORIGINS`, `WEATHER_CACHE_TTL_SECONDS`.

### API contract (unchanged)

```
POST /api/chat
Body: { session_id, location, message? }
Response: { session_id, answer, weather_summary, cache_hit }
```

### LLM fallback order (unchanged)

Ollama → OpenAI → Anthropic. Controlled by env vars.

## Testing Decisions

A good test verifies observable external behaviour — what the module returns or what side effects it produces — not how it is internally implemented.

**Existing test coverage to keep green:**
- `tests/agents/` — outfit agent, cache agent, LLM factory (all mocked at the HTTP boundary)
- `tests/api/test_endpoints.py` — FastAPI endpoint integration tests
- `tests/tools/` — Redis and HTTP tool unit tests

**New tests for this PRD:**
- None required for MVP. The changes are thin wiring (config defaults, env vars, Docker plumbing) that are better validated by running the stack than by unit tests.
- If Vite proxy config is added, a manual smoke test (dev server → backend) is sufficient.

**What would be worth testing later (post-MVP):**
- Frontend component tests (Vitest) for ChatWindow — especially the error state rendering and cache badge display logic.
- Docker Compose smoke test: `curl http://localhost/api/health` returns `{"status":"ok"}`.

## Out of Scope

- Bulma or any CSS framework redesign (create a separate issue)
- Wardrobe photo uploads
- Multi-city packing lists
- Severe weather alerts
- User accounts or authentication
- Subscription pricing tiers
- Style as a structured dropdown (free text is sufficient for MVP)
- Persistent chat history across sessions
- Mobile-responsive layout improvements

## Further Notes

- Ollama must be running on the host and `gemma4:e2b` must be pulled (`ollama pull gemma4:e2b`) before `docker-compose up`. Document this in the README as a prerequisite.
- `gemma4:e2b` is 7.2 GB. Ensure the showcase machine has it pre-pulled before the presentation.
- The `cache_hit` badge is the clearest way to demo Redis live — run the same city twice and show the second response is instant with the badge.
- CORS is set to `*` for MVP. Before any public deployment, lock it to the actual frontend origin.
