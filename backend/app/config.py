# backend/app/config.py
# Single source of truth for all environment variables.
# Import `settings` wherever you need a config value — never read os.environ directly.

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    anthropic_api_key:         str
    anthropic_model:           str = "claude-3-5-haiku-20241022"
    weather_cache_ttl_seconds: int = 1800
    sqlite_db_path:            str = "weather_cache.db"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
