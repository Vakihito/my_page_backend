from src.shared.database_shared import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import (
    Column,
    String,
    DateTime,
    text,
)


class UserModel(Base):
    __tablename__ = "user"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        nullable=False,
    )
    name = Column(String, nullable=False)
    start_date = Column(DateTime, server_default=text("NOW()"), nullable=True)
    end_date = Column(DateTime, server_default=text("NOW()"), nullable=True)
    date_format = Column(String, server_default="weaks", nullable=True)
    created_at = Column(DateTime, server_default=text("NOW()"), nullable=True)
    deleted_at = Column(DateTime, server_default=None, nullable=True)
