# feat: multi-stage frontend Dockerfile and Nginx config

**Type:** AFK  
**Blocked by:** issue-2

## What to build

Add a multi-stage Dockerfile for the frontend: stage 1 runs `vite build`, stage 2 serves the `dist/` output with Nginx alpine. Include an `nginx.conf` that serves the Vue SPA (all unmatched routes return `index.html`) and proxies `/api/` to the backend service.

## Acceptance criteria

- [ ] `frontend/Dockerfile` builds successfully with `docker build frontend/`
- [ ] `frontend/nginx.conf` serves SPA correctly (direct URL access to a Vue route returns `index.html`)
- [ ] `/api/` is proxied to `http://backend:8000/`
- [ ] Built image is reasonably small (Nginx alpine base)
