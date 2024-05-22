from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@0.0.0.0:5433/postgres"
    TEST_DATABASE_URL: str = "postgresql://postgres:postgres@0.0.0.0:5433/postgres_test"
    LOG_LEVEL: str = "INFO"
    LOG_LEVEL_DB: str = "ERROR"
    TESTING: bool = False

    class Config:
        env_file = ".env"


def get_settings() -> Settings:
    return Settings()
