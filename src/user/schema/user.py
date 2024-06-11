from uuid import UUID
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field


class CreateUserInputSchema(BaseModel):
    id: UUID = Field(default=None)
    name: str = Field(default=None)
    start_date: datetime = Field(default=None)
    end_date: datetime = Field(default=None)
    date_format: str = Field(default=None)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "todo",
                "start_date": "2024-06-07",
                "end_date": "2024-06-07",
                "date_format": "weaks",
            }
        }


class CreateUserResponseSchema(BaseModel):
    created: bool
