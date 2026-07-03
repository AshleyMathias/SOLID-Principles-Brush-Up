from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Production Chabot API"
    API_VERSION: str = "v1"

    ENVIRONMENT: str = Field(...)

    OPENAI_API_KEY: str = Field(...)

    DATABASE_URL: str = Field(...)

    REDIS_URL: str = Field(...)

    SECRET_KEY: str = Field(...)

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()