from src.goals.schema import SearchGoalsInputSchema, CreateGoalInputSchema
from src.goals.model import GoalsModel
from src.goals.infra import GoalsRepository
from typing import List, Literal, Optional, Union


class SearchGoalsService:
    def __init__(
        self, search_goals_repository: GoalsRepository
    ) -> List[CreateGoalInputSchema]:
        self.search_goals_repository = search_goals_repository

    def search_goals(self, **args) -> List[CreateGoalInputSchema]:
        serach_input = SearchGoalsInputSchema(**args)
        print(f"searching for : {serach_input}")
        searched_object = self.search_goals_repository.search_goals(serach_input)
        print(f"searched_object : {searched_object}")
        return searched_object
