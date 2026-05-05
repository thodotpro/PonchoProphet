import pytest
from unittest.mock import patch, AsyncMock
from agents.llm_factory import get_llm
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic


async def test_get_llm_prefers_ollama_when_available():
    with patch("agents.llm_factory.is_ollama_online", new_callable=AsyncMock, return_value=True):
        llm = await get_llm()
        assert isinstance(llm, ChatOllama)
        assert llm.model == "gemma2:2b"


async def test_get_llm_falls_back_to_openai():
    with patch("agents.llm_factory.is_ollama_online", new_callable=AsyncMock, return_value=False):
        with patch("agents.llm_factory.settings") as mock_settings:
            mock_settings.openai_api_key = "sk-test-key"
            mock_settings.openai_model = "gpt-4o-mini"
            llm = await get_llm()
            assert isinstance(llm, ChatOpenAI)
            assert llm.model_name == "gpt-4o-mini"


async def test_get_llm_falls_back_to_anthropic():
    with patch("agents.llm_factory.is_ollama_online", new_callable=AsyncMock, return_value=False):
        with patch("agents.llm_factory.settings") as mock_settings:
            mock_settings.openai_api_key = None
            mock_settings.anthropic_api_key = "ant-test-key"
            mock_settings.anthropic_model = "claude-test"
            llm = await get_llm()
            assert isinstance(llm, ChatAnthropic)
            assert llm.model == "claude-test"


async def test_get_llm_raises_error_when_no_provider():
    with patch("agents.llm_factory.is_ollama_online", new_callable=AsyncMock, return_value=False):
        with patch("agents.llm_factory.settings") as mock_settings:
            mock_settings.openai_api_key = None
            mock_settings.anthropic_api_key = None
            with pytest.raises(ValueError, match="No LLM provider available"):
                await get_llm()
