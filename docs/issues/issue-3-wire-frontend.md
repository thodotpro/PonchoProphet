# feat: wire frontend to backend and add Vite dev proxy

**Type:** AFK  
**Blocked by:** issue-1, issue-2

## What to build

Remove the mock response block from ChatWindow and activate the real `fetch('/api/chat', ...)` call. Add a `vite.config.js` with a dev server proxy so `/api` forwards to `http://localhost:8000` in development. End-to-end flow should be demoable with `npm run dev` + local uvicorn.

## Acceptance criteria

- [ ] `vite.config.js` exists with `server.proxy` forwarding `/api` → `http://localhost:8000`
- [ ] Mock block removed from `ChatWindow.vue`
- [ ] Real fetch is active and sends `{ session_id, location, message }`
- [ ] Network errors, 422, and 503 responses surface as error messages in the chat
- [ ] Cache badge shows on `cache_hit: true` responses
- [ ] Weather summary bar updates on each response
