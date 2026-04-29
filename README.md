# PonchoProphet 🌦️🧥

PonchoProphet is a smart outfit advisor that provides personalized clothing recommendations based on real-time weather data. It's designed to be a robust, "one-click" project for university demonstrations, featuring local-first AI and a deterministic processing pipeline.

## 🚀 Quick Start (One-Click Setup)

The entire stack is orchestrated via Docker. Ensure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

1. **Clone the repository.**
2. **Start the application:**
   ```bash
   docker-compose up --build
   ```
3. **Wait for the models:** 
   On the first run, the system will automatically pull the `gemma2:2b` model into the local Ollama container. The backend will start accepting requests once the download is complete.
4. **Access the UI:**
   Open `http://localhost:5173` in your browser.

---

## 🧠 Backend Architecture

The backend is built with **FastAPI** and **LangGraph**, providing a modular and predictable flow for every request:

1. **Geocoding:** Converts user input (e.g., "Vienna") into coordinates using Open-Meteo.
2. **Caching:** Checks **Redis** for fresh weather data to minimize API calls.
3. **Weather Fetch:** If not cached, retrieves real-time data from Open-Meteo.
4. **LLM Recommendation:** Generates the outfit advice using a prioritized fallback chain.

### 🤖 Multi-LLM Fallback Logic
PonchoProphet is designed to be cost-effective and flexible. It automatically selects the best available LLM:

*   **Priority 1: Ollama (Local)** – Runs `gemma2:2b` locally on your machine. Zero cost, 100% private.
*   **Priority 2: OpenAI** – Falls back to `gpt-4o-mini` if an `OPENAI_API_KEY` is provided and Ollama is unreachable.
*   **Priority 3: Anthropic** – Last resort using `claude-3-5-haiku` if an `ANTHROPIC_API_KEY` is provided.

### 📦 Tech Stack
- **AI Framework:** LangChain / LangGraph
- **Database/Cache:** Redis
- **Package Manager:** `uv` (Fast and reliable Python dependency management)
- **API Framework:** FastAPI
- **Deployment:** Docker Compose

---

## 🛠️ Configuration

While the project works out-of-the-box with Ollama, you can configure cloud providers by adding a `.env` file in the `backend/` directory:

```env
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
```

---

## 🧪 Development & Testing

The project uses `uv` for local development. To run tests:

```bash
cd backend
uv sync
uv run pytest
```
