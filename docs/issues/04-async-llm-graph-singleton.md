# [ISSUE-04] Async LLM node & graph singleton

**Labels:** needs-triage  
**Type:** AFK

## What to build

Switch `outfit_node` from `llm.invoke()` to `await llm.ainvoke()`. Move `build_graph()` to module level so the compiled pipeline is a singleton reused across all requests. Add a startup warning in the FastAPI lifespan hook if no LLM provider is configured. Include a test for `outfit_node`.

Demoable by: observing no graph compilation log on the second request; confirming `outfit_node` returns a non-empty answer string.

## Acceptance criteria

- [ ] `outfit_node` is `async def` and uses `await llm.ainvoke(messages)`
- [ ] `build_graph()` is called once at module/app startup, not inside the route handler
- [ ] The compiled graph object is reused across all `POST /chat` requests
- [ ] FastAPI lifespan hook logs a WARNING if no LLM provider is available at startup
- [ ] Unit test: `outfit_node` returns non-empty string in `answer` field (LLM mocked)
- [ ] End-to-end smoke: `POST /chat` with mocked IO completes without error

## Blocked by

- ISSUE-02 (all nodes must be async before graph is assembled)
- ISSUE-03 (all nodes must be async before graph is assembled)
