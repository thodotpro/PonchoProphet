# [ISSUE-02] Async Redis cache layer

**Labels:** needs-triage  
**Type:** AFK

## What to build

Convert the Redis client and all cache tools to use `redis.asyncio` so cache lookups and writes are non-blocking. Add graceful degradation so a Redis outage causes a cache miss (pipeline continues) rather than an unhandled 500. Include tests for the cache tool and cache node.

Demoable by: starting the server with Redis offline and confirming requests still succeed (with a cache-miss path); confirming no event loop blocking under concurrent load.

## Acceptance criteria

- [ ] `redis_client.py` uses `redis.asyncio` and exposes an async client
- [ ] `query_db` is `async def`; returns `None` on Redis error (logged at WARNING, not raised)
- [ ] `save_db` is `async def`; catches and logs Redis errors without raising
- [ ] `cache_node` is `async def`
- [ ] Server starts and serves requests normally when Redis is unreachable
- [ ] Unit test: `query_db` returns cached dict on hit
- [ ] Unit test: `query_db` returns `None` on miss
- [ ] Unit test: `query_db` returns `None` on Redis connection error (no exception propagated)
- [ ] Unit test: `save_db` does not raise on Redis connection error
- [ ] Unit test: `cache_node` sets `cache_hit=True` + `weather` on hit
- [ ] Unit test: `cache_node` sets `cache_hit=False` on miss
- [ ] Unit test: `cache_node` sets `cache_hit=False` on Redis error

## Blocked by

None — can start immediately.
