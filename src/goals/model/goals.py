from src.shared.database_shared import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import (
    Column,
    String,
    DateTime,
    text,
)


class GoalsModel(Base):
    __tablename__ = "goals"

    id = Column(
        UUID(as_uuid=True),
        server_default=text("NOW()"),
        primary_key=True,
        index=True,
        nullable=False,
    )
    title = Column(String, nullable=False)
    todo = Column(String, nullable=True)
    nottodo = Column(String, nullable=True)
    start_date = Column(DateTime, server_default=text("NOW()"), nullable=True)
    end_date = Column(DateTime, server_default=text("NOW()"), nullable=True)
    data_format = Column(String, server_default="weaks", nullable=True)
    created_at = Column(DateTime, server_default=text("NOW()"), nullable=True)
    deleted_at = Column(DateTime, server_default=None, nullable=True)
