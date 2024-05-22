import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.main.settings import get_settings

# Helper function to get database session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main.settings import get_settings

settings = get_settings()


def get_session(database_url):
    engine = create_engine(
        database_url,
        pool_size=30,
        max_overflow=0,
        connect_args={"connect_timeout": 30},
    )
    Session = sessionmaker(autocommit=False, autoflush=True, bind=engine)
    return Session


logging.getLogger("sqlalchemy.engine.Engine").setLevel(settings.LOG_LEVEL_DB)
logging.getLogger("sqlalchemy.pool").setLevel(settings.LOG_LEVEL_DB)

Base = declarative_base()
SessionLocal = get_session(settings.DATABASE_URL)
TestingSessionLocal = get_session(settings.TEST_DATABASE_URL)

def get_db_session():
    db = SessionLocal() if not settings.TESTING else TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
