from uuid import UUID
from datetime import date, datetime
from pydantic import BaseModel


class CreateGoalInputSchema(BaseModel):
    id: UUID
    title: str


class CreateGoalResponseSchema(BaseModel):
    created: bool
