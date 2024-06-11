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
