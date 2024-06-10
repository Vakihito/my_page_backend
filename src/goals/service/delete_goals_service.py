from src.goals.schema import DeleteGoalsInputSchema, DeleteGoalsResponseSchema
from src.goals.model import GoalsModel
from src.goals.infra import GoalsRepository


class DeleteGoalsService:
    def __init__(self, delete_goals_repository: GoalsRepository) -> DeleteGoalsResponseSchema:
        self.delete_goals_repository = delete_goals_repository

    def delete_goals(self, delete_goals_input: DeleteGoalsInputSchema) -> DeleteGoalsResponseSchema:
        if delete_goals_input.is_soft:
            self.delete_goals_repository.delete_goals(delete_goals_input)
        else:
            self.delete_goals_repository.delete_goals_hard(delete_goals_input)
        return {"deleted": True}
