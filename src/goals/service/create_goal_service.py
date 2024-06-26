from src.goals.schema import CreateGoalInputSchema, CreateGoalResponseSchema
from src.goals.model import GoalsModel
from src.goals.infra import GoalsRepository
from uuid import uuid4


class CreateGoalService:
    def __init__(self, create_goal_repository: GoalsRepository) -> CreateGoalResponseSchema:
        self.create_goal_repository = create_goal_repository

    def create(self, create_goal_input: CreateGoalInputSchema) -> CreateGoalResponseSchema:
        if create_goal_input.id is None:
            create_goal_input.id = uuid4()
        create_goal_reseponse = self.create_goal_repository.create_goal(create_goal_input)
        if create_goal_reseponse is not None:
            create_goal_reseponse = {"created": True}
        else:
            create_goal_reseponse = {"created": False}
        return create_goal_reseponse
