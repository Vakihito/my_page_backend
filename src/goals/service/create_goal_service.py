from src.goals.schema import CreateGoalInputSchema, CreateGoalResponseSchema


class CreateGoalService:
    def __init__(self) -> CreateGoalResponseSchema:
        self.repo = None

    def create(
        self, create_goal_input: CreateGoalInputSchema
    ) -> CreateGoalResponseSchema:
        create_goal_reseponse = {"created": True}
        return create_goal_reseponse
