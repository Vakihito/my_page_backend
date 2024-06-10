from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@postgres:5432/postgres"
    TEST_DATABASE_URL: str = "postgresql://postgres:postgres@postgres:5432/postgres_test"
    LOG_LEVEL: str = "INFO"
    LOG_LEVEL_DB: str = "ERROR"
    TESTING: bool = False
    CHOKIDAR_USEPOLLING: bool = True
    FAST_REFRESH: bool = True

    class Config:
        env_file = ".env"


def get_settings() -> Settings:
    return Settings()
