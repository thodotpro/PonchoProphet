# PonchoProphet 🌦️🧥

Smart outfit recommendations driven by real-time weather data and a multi-LLM backend.

---

## Requirements

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows / macOS) or Docker Engine + Compose plugin (Linux)
- [Ollama](https://ollama.com/download) installed and running **on your host machine** (not inside Docker)

> Ollama must be running before you start the stack. The backend reaches it via `host.docker.internal`.

---

## Quick start

### 1. Pull the model

```bash
ollama pull gemma4:e2b
```

### 2. Clone and configure

```bash
git clone https://github.com/thodotpro/PonchoProphet.git
cd PonchoProphet
cp .env.example .env
```

Edit `.env` if you want to use a different model or add cloud API keys (see [Configuration](#configuration)).

### 3. Start the stack

**Linux / macOS**
```bash
docker compose up --build
```

**Windows (PowerShell)**
```powershell
docker compose up --build
```

### 4. Open the app

```
http://localhost
```

---

## Windows notes

- Use **Docker Desktop for Windows** (WSL 2 backend recommended).
- Ollama for Windows runs as a background tray app — start it before running `docker compose`.
- Run commands in **PowerShell** or **Windows Terminal**. Command Prompt works too.
- If `localhost` doesn't load, try `http://127.0.0.1`.

## Linux notes

- Docker Engine with the Compose plugin is enough — Docker Desktop is optional.
- Check Docker is running: `sudo systemctl start docker` (if not already).
- Ollama can be installed via the official script and runs as a systemd service:
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ollama serve &   # or: sudo systemctl start ollama
  ```
- If you get permission errors: add your user to the `docker` group with `sudo usermod -aG docker $USER`, then log out and back in.

---

## Configuration

Copy `.env.example` to `.env` in the project root and edit as needed:

| Variable | Default | Description |
|---|---|---|
| `OLLAMA_MODEL` | `gemma4:e2b` | Local model to use |
| `OLLAMA_BASE_URL` | `http://localhost:11434` | Ollama host URL |
| `ANTHROPIC_API_KEY` | _(empty)_ | Fallback to Claude if Ollama is unavailable |
| `OPENAI_API_KEY` | _(empty)_ | Fallback to GPT if Ollama is unavailable |
| `OPENAI_BASE_URL` | _(empty)_ | Override for OpenAI-compatible providers (e.g. Groq) |
| `OPENAI_MODEL` | `gpt-4o-mini` | Model used when falling back to OpenAI |
| `WEATHER_CACHE_TTL_SECONDS` | `1800` | How long weather data is cached (seconds) |

---

## LLM fallback chain

The backend automatically selects the best available provider:

1. **Ollama (local)** — zero cost, fully private, runs on your machine
2. **OpenAI** — used if `OPENAI_API_KEY` is set and Ollama is unreachable
3. **Anthropic** — last resort if `ANTHROPIC_API_KEY` is set

---

## Architecture

```
Browser → nginx (port 80) → /api/* → FastAPI backend → LangGraph pipeline
                                                       ├── Geocoding (Open-Meteo)
                                                       ├── Weather fetch + Redis cache
                                                       └── LLM recommendation
```

- **Frontend**: Vue 3 + Vite, served by nginx with SPA fallback
- **Backend**: FastAPI + LangGraph, Python 3.12, managed with `uv`
- **Cache**: Redis 7
- **AI**: Ollama (local) with OpenAI / Anthropic cloud fallback

---

## Local development (without Docker)

**Backend**
```bash
cd backend
uv sync
uv run uvicorn app.main:app --reload
```

**Frontend**
```bash
cd frontend
npm install
npm run dev   # http://localhost:5173
```

**Tests**
```bash
cd backend
uv run pytest
```
