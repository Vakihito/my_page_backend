from src.goals.service import UpdateGoalsService
from src.goals.schema import CreateGoalInputSchema, UpdateGoalsResponseSchema
from starlette import status
from fastapi import APIRouter, Body, Depends


class UpdateGoalsController:
    def __init__(self, update_goals_service: UpdateGoalsService):
        self.update_goals_service = update_goals_service
        self.router = APIRouter()
        self.router.add_api_route(
            "/update_goals",
            self.handle,
            methods=["POST"],
            status_code=status.HTTP_200_OK,
            response_model=UpdateGoalsResponseSchema,
            name="Update new goal",
        )

    async def handle(self, update_goals_input: CreateGoalInputSchema):
        return self.update_goals_service.update_goals(update_goals_input)
