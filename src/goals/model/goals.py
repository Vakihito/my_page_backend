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

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, nullable=False)
    title = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=text("NOW()"))
