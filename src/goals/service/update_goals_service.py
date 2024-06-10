from src.goals.schema import CreateGoalInputSchema, UpdateGoalsResponseSchema
from src.goals.model import GoalsModel
from src.goals.infra import GoalsRepository



class UpdateGoalsService:
    def __init__(
        self, update_goals_repository: GoalsRepository
    ) -> UpdateGoalsResponseSchema:
        self.update_goals_repository = update_goals_repository

    def update_goals(
        self, update_goals_input: CreateGoalInputSchema
    ) -> UpdateGoalsResponseSchema:
        response = self.update_goals_repository.update_goals(update_goals_input)
        created = False
        if response is not None:
            created = True
        return {"updated": created}
