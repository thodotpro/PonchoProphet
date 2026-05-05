import logging

import httpx
from app.config import settings
from langchain_anthropic import ChatAnthropic
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

logger = logging.getLogger(__name__)


async def is_ollama_online() -> bool:
    """Check if the local Ollama service is reachable and has the configured model."""
    try:
        async with httpx.AsyncClient(timeout=1.0) as client:
            response = await client.get(f"{settings.ollama_base_url}/api/tags")
        if response.status_code != 200:
            return False
        models = [m["name"] for m in response.json().get("models", [])]
        return any(settings.ollama_model in m for m in models)
    except (httpx.RequestError, httpx.ConnectError):
        return False


async def get_llm() -> BaseChatModel:
    """
    Factory returning the highest-priority available LLM.
    Priority: Ollama -> OpenAI -> Anthropic
    """
    if await is_ollama_online():
        logger.info("LLM provider selected: ollama (%s)", settings.ollama_model)
        return ChatOllama(model=settings.ollama_model, base_url=settings.ollama_base_url)

    if settings.openai_api_key:
        logger.info("LLM provider selected: openai (%s)", settings.openai_model)
        return ChatOpenAI(model=settings.openai_model, api_key=settings.openai_api_key)

    if settings.anthropic_api_key:
        logger.info("LLM provider selected: anthropic (%s)", settings.anthropic_model)
        return ChatAnthropic(model=settings.anthropic_model, api_key=settings.anthropic_api_key)

    raise ValueError(
        "No LLM provider available. Please set OPENAI_API_KEY, "
        "ANTHROPIC_API_KEY, or ensure Ollama is running."
    )
