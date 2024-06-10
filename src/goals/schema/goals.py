from uuid import UUID, uuid4
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field


class CreateGoalInputSchema(BaseModel):
    id: UUID = uuid4()
    title: str = Field(default=None)
    todo: str = Field(default=None)
    nottodo: str = Field(default=None)
    start_date: datetime = Field(default=None)
    end_date: datetime = Field(default=None)
    data_format: str = Field(default=None)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "title",
                "todo": "todo",
                "nottodo": "notodo",
                "start_date": "2024-06-07",
                "end_date": "2024-06-07",
                "data_format": "weaks",
            }
        }


class CreateGoalResponseSchema(BaseModel):
    created: bool


class UpdateGoalsResponseSchema(BaseModel):
    updated: bool


class DeleteGoalsInputSchema(BaseModel):
    id: UUID
    is_soft: bool = True


class DeleteGoalsResponseSchema(BaseModel):
    deleted: bool


class SearchGoalsInputSchema(BaseModel):
    text_title: str | None = None
