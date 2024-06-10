from src.goals.service import SearchGoalsService
from src.goals.schema import SearchGoalsInputSchema, CreateGoalInputSchema
from starlette import status
from fastapi import APIRouter, Body, Depends
from typing import List, Literal, Optional, Union


class SearchGoalsController:
    def __init__(self, search_goals_service: SearchGoalsService):
        self.search_goals_service = search_goals_service
        self.router = APIRouter()
        self.router.add_api_route(
            "/search_goals/{text_title}",
            self.handle,
            methods=["GET"],
            status_code=status.HTTP_200_OK,
            response_model=List[CreateGoalInputSchema],
            name="",
        )

    async def handle(self, text_title: str) -> List[CreateGoalInputSchema]:
        return self.search_goals_service.search_goals(text_title=text_title)
