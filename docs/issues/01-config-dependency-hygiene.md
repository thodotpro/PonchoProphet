# [ISSUE-01] Config & dependency hygiene

**Labels:** needs-triage  
**Type:** AFK

## What to build

Lock down CORS to specific methods and headers, update the Anthropic model ID to the current Haiku release, pin all LangChain/LangGraph package versions, add INFO-level logging when the LLM factory selects a provider, and add `pytest-asyncio` to test dependencies.

This slice has no runtime logic changes — it is purely configuration and dependency correctness. Demoable by: running the server and confirming CORS headers in devtools; checking `requirements.txt` is fully pinned; seeing a log line like `INFO: LLM provider selected: ollama (gemma2:2b)` on startup/request.

## Acceptance criteria

- [ ] `allow_methods` in CORS middleware is `["GET", "POST"]` (not `["*"]`)
- [ ] `allow_headers` in CORS middleware is `["Content-Type"]` (not `["*"]`)
- [ ] Default Anthropic model in config is `claude-haiku-4-5-20251001`
- [ ] All `langchain-*` and `langgraph` packages have pinned version numbers in `requirements.txt`
- [ ] `pytest-asyncio` is present in `requirements.txt`
- [ ] `get_llm()` logs at INFO level which provider and model was selected
- [ ] Existing `test_llm_factory.py` still passes after changes

## Blocked by

None — can start immediately.
