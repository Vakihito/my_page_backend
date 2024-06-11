from src.goals.schema import CreateGoalInputSchema
from src.goals.model import GoalsModel
from src.goals.infra import GoalsRepository


class GetByUserGoalsService:
    def __init__(
        self, get_by_user_goals_repository: GoalsRepository
    ) -> CreateGoalInputSchema:
        self.get_by_user_goals_repository = get_by_user_goals_repository

    def get_by_user_goals(self, get_by_user_goals: str) -> CreateGoalInputSchema:
        get_by_user_goals = self.get_by_user_goals_repository.get_by_user_goals(
            get_by_user_goals
        )
        return get_by_user_goals
