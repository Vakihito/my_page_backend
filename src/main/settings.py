from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@postgres:5432/postgres"
    TEST_DATABASE_URL: str = (
        "postgresql://postgres:postgres@postgres:5432/postgres_test"
    )

    class Config:
        env_file = ".env"


def get_settings() -> Settings:
    return Settings()
