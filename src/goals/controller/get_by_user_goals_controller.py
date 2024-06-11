from src.goals.service import GetByUserGoalsService
from src.goals.schema import CreateGoalInputSchema
from starlette import status
from fastapi import APIRouter, Body, Depends


class GetByUserGoalsController:
    def __init__(self, get_by_user_goals_service: GetByUserGoalsService):
        self.get_by_user_goals_service = get_by_user_goals_service
        self.router = APIRouter()
        self.router.add_api_route(
            "/get_by_user_goals/{user_id}",
            self.handle,
            methods=["GET"],
            status_code=status.HTTP_200_OK,
            response_model=list[CreateGoalInputSchema],
            name="",
        )

    async def handle(self, user_id: str) -> list[CreateGoalInputSchema]:
        return self.get_by_user_goals_service.get_by_user_goals(user_id)
