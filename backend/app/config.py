# backend/app/config.py
# Single source of truth for all environment variables.
# Import `settings` wherever you need a config value — never read os.environ directly.

from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    anthropic_api_key:         Optional[str] = None
    anthropic_model:           str = "claude-3-5-haiku-20241022"
    
    openai_api_key:            Optional[str] = None
    openai_model:              str = "gpt-4o-mini"
    
    ollama_base_url:           str = "http://localhost:11434"
    ollama_model:              str = "gemma2:2b"

    weather_cache_ttl_seconds: int = 1800
    redis_url:                 str = "redis://localhost:6379/0"
    allowed_origins:           str = "http://localhost:5173"

    @property
    def allowed_origins_list(self) -> list[str]:
        return [s.strip() for s in self.allowed_origins.split(",")]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
