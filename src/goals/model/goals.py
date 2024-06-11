from src.shared.database_shared import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import (
    Column,
    String,
    DateTime,
    ForeignKey,
    text,
)


class GoalsModel(Base):
    __tablename__ = "goals"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        nullable=False,
    )
    title = Column(String, nullable=False, index=True)
    todo = Column(String, nullable=True, index=True)
    nottodo = Column(String, nullable=True, index=True)
    start_date = Column(DateTime, server_default=text("NOW()"), nullable=True)
    end_date = Column(DateTime, server_default=text("NOW()"), nullable=True)
    date_format = Column(String, server_default="weaks", nullable=True)
    created_at = Column(DateTime, server_default=text("NOW()"), nullable=True)
    deleted_at = Column(DateTime, server_default=None, nullable=True)
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("user.id"),
        index=True,
        nullable=False,
    )
