from uuid import UUID
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict


class CreateGoalInputSchema(BaseModel):
    id: UUID
    title: str
    model_config = ConfigDict(id="00000000-0000-0000-0000-000000000000",
                title="cool little text",
            )


class CreateGoalResponseSchema(BaseModel):
    created: bool
