# feat: update config defaults and add .env.example

**Type:** AFK  
**Blocked by:** None — can start immediately

## What to build

Update the backend config to use `gemma4:e2b` as the default Ollama model and open CORS to `*` for the MVP showcase. Create an `.env.example` file documenting every environment variable so any team member can configure the stack without reading source code.

## Acceptance criteria

- [ ] `ollama_model` default is `gemma4:e2b`
- [ ] `allowed_origins` default is `*`
- [ ] `.env.example` exists at repo root documenting: `OLLAMA_MODEL`, `OLLAMA_BASE_URL`, `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `REDIS_URL`, `ALLOWED_ORIGINS`, `WEATHER_CACHE_TTL_SECONDS`
- [ ] Existing tests still pass
