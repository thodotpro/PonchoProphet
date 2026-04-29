import httpx
from app.config import settings
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.language_models.chat_models import BaseChatModel


def is_ollama_online() -> bool:
    """Check if the local Ollama service is reachable and has the model."""
    try:
        # Check if service is up
        response = httpx.get(f"{settings.ollama_base_url}/api/tags", timeout=1.0)
        if response.status_code != 200:
            return False
        
        # Check if the specific model is already pulled
        models = [m["name"] for m in response.json().get("models", [])]
        # Ollama sometimes appends :latest or other tags, so we check for partial match
        return any(settings.ollama_model in m for m in models)
    except (httpx.RequestError, httpx.ConnectError):
        return False


def get_llm() -> BaseChatModel:
    """
    Factory to return the highest priority available LLM.
    Priority: Ollama -> OpenAI -> Anthropic
    """
    # 1. Check Ollama
    if is_ollama_online():
        return ChatOllama(
            model=settings.ollama_model,
            base_url=settings.ollama_base_url,
        )

    # 2. Check OpenAI
    if settings.openai_api_key:
        return ChatOpenAI(
            model=settings.openai_model,
            api_key=settings.openai_api_key,
        )

    # 3. Check Anthropic
    if settings.anthropic_api_key:
        return ChatAnthropic(
            model=settings.anthropic_model,
            api_key=settings.anthropic_api_key,
        )

    raise ValueError(
        "No LLM provider available. Please set OPENAI_API_KEY, "
        "ANTHROPIC_API_KEY, or ensure Ollama is running."
    )
