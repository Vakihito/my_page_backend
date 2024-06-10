from src.goals.service import DeleteGoalsService
from src.goals.schema import DeleteGoalsInputSchema, DeleteGoalsResponseSchema
from starlette import status
from fastapi import APIRouter, Body, Depends


class DeleteGoalsController:
    def __init__(self, delete_goals_service: DeleteGoalsService):
        self.delete_goals_service = delete_goals_service
        self.router = APIRouter()
        self.router.add_api_route(
            "/delete_goals",
            self.handle,
            methods=["DELETE"],
            status_code=status.HTTP_204_NO_CONTENT,
            name="Delete a goal",
            description="Soft Deletes a goal based on a id",
        )

    async def handle(self, delete_goals_input: DeleteGoalsInputSchema):
        return self.delete_goals_service.delete_goals(delete_goals_input)
