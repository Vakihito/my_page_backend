from uuid import UUID
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict


class CreateUserInputSchema(BaseModel):
    some_data: bool


class CreateUserResponseSchema(BaseModel):
    created: bool
