import pytest
from unittest.mock import patch, MagicMock
from agents.llm_factory import get_llm
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

def test_get_llm_prefers_ollama_when_available():
    # Mocking httpx or a similar check to simulate Ollama being "up"
    with patch("agents.llm_factory.is_ollama_online", return_value=True):
        llm = get_llm()
        assert isinstance(llm, ChatOllama)
        assert llm.model == "gemma2:2b"

def test_get_llm_falls_back_to_openai():
    with patch("agents.llm_factory.is_ollama_online", return_value=False):
        # Mock settings to have OpenAI key but not Ollama
        with patch("agents.llm_factory.settings") as mock_settings:
            mock_settings.openai_api_key = "sk-test-key"
            mock_settings.openai_model = "gpt-4o-mini"
            llm = get_llm()
            assert isinstance(llm, ChatOpenAI)
            assert llm.model_name == "gpt-4o-mini"

def test_get_llm_falls_back_to_anthropic():
    with patch("agents.llm_factory.is_ollama_online", return_value=False):
        with patch("agents.llm_factory.settings") as mock_settings:
            mock_settings.openai_api_key = None
            mock_settings.anthropic_api_key = "ant-test-key"
            mock_settings.anthropic_model = "claude-test"
            llm = get_llm()
            assert isinstance(llm, ChatAnthropic)
            assert llm.model == "claude-test"

def test_get_llm_raises_error_when_no_provider():
    with patch("agents.llm_factory.is_ollama_online", return_value=False):
        with patch("agents.llm_factory.settings") as mock_settings:
            mock_settings.openai_api_key = None
            mock_settings.anthropic_api_key = None
            with pytest.raises(ValueError, match="No LLM provider available"):
                get_llm()
