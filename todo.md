# Project State & Production Plan

## Backend Status: [READY FOR PROD]
Refactored for scalability, persistence, and production-grade serving.

### Changes Made:
- **Cache Engine**: Migrated from SQLite to **Redis**.
  - Faster lookups, central persistence, automatic TTL handling.
  - New `backend/tools/redis_client.py` for shared connection.
- **Web Server**: Updated `Dockerfile` to use **Gunicorn** with `UvicornWorker`.
  - Enables multiple workers for concurrent request handling.
- **Security**: Implemented environment-based **CORS** via `ALLOWED_ORIGINS`.
  - Supports comma-separated list of domains.
- **Configuration**: Enhanced `backend/app/config.py` using Pydantic Settings.
  - Added `REDIS_URL` and `ALLOWED_ORIGINS` with defaults for local dev.
- **Infrastructure**: Updated `docker-compose.yml` to include a Redis service.

### Todo / Next Steps:
- [ ] Implement GitHub Actions for automated deployment to Render.
- [ ] Add unit/integration tests for Redis cache logic.
- [ ] Set up monitoring (e.g., Sentry) for pipeline errors.

---

## Frontend Status: [MVP / NEEDS PROD SYNC]
Currently configured for local development.

### Current State:
- **Framework**: Vue 3 + Vite.
- **API Integration**: Hardcoded to `localhost:8000`.
- **Styling**: Vanilla CSS (modern/interactive).

### Todo / Next Steps:
- [ ] **Env Var Sync**: Use `import.meta.env.VITE_API_URL` instead of hardcoded localhost.
- [ ] **Deployment**: Build static assets and host on Vercel or Netlify.
- [ ] **Error Handling**: Add UI feedback for backend 422 (geocoding) and 500 errors.
- [ ] **Loading States**: Improve "StatusBadge" to show granular graph steps if possible.

---

## Global Stack:
- **LLM**: Anthropic Claude 3.5 Haiku.
- **Orchestration**: LangGraph.
- **API**: FastAPI.
- **Cache**: Redis.
- **Hosting Target**: Render (Backend), Vercel/Netlify (Frontend).
