# feat: docker-compose for one-command showcase

**Type:** AFK  
**Blocked by:** issue-1, issue-3, issue-4

## What to build

Add a `docker-compose.yml` at the repo root that starts three services: `redis`, `backend`, and `frontend`. The backend service must be able to reach the host Ollama instance. Running `docker-compose up` should bring the full stack up and serve the app at `http://localhost`.

## Acceptance criteria

- [ ] `docker-compose up` starts redis, backend, and frontend without errors
- [ ] App is accessible at `http://localhost`
- [ ] Backend reaches host Ollama via `host.docker.internal:11434` (works on Linux, Mac, Windows)
- [ ] `extra_hosts: ["host.docker.internal:host-gateway"]` present for Linux compatibility
- [ ] Backend env vars injected: `REDIS_URL=redis://redis:6379/0`, `OLLAMA_BASE_URL=http://host.docker.internal:11434`, `OLLAMA_MODEL=gemma4:e2b`, `ALLOWED_ORIGINS=*`
- [ ] `GET http://localhost/api/health` returns `{"status":"ok"}`
- [ ] Full chat flow works end-to-end
