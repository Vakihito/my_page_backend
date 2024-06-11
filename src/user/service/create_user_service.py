from src.user.schema import CreateUserInputSchema, CreateUserResponseSchema
from src.user.model import GoalsModel
from src.user.infra import GoalsRepository


class CreateUserService:
    def __init__(self, create_user_repository: GoalsRepository) -> CreateUserResponseSchema:
        self.create_user_repository = create_user_repository

    def create_user(self, create_user_input: CreateUserInputSchema) -> CreateUserResponseSchema:
        return {"created": True}
