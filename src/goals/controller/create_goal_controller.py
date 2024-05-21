from src.goals.service import CreateGoalService
from src.goals.schema import CreateGoalInputSchema, CreateGoalResponseSchema
from starlette import status

from fastapi import APIRouter, Body, Depends


class CreateGoalController:
    def __init__(self, create_goal_service: CreateGoalService):
        self.create_goal_service = create_goal_service
        self.router = APIRouter()
        self.router.add_api_route(
            "/create_goal",
            self.handle,
            methods=["POST"],
            status_code=status.HTTP_201_CREATED,
            response_model=CreateGoalResponseSchema,
            name="Create a new goal",
        )

    async def handle(self, create_goal_input: CreateGoalInputSchema):
        return self.create_goal_service.create(create_goal_input)
