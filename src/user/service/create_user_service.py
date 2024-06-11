from src.user.schema import CreateUserInputSchema, CreateUserResponseSchema
from src.user.model import UserModel
from src.user.infra import UserRepository


class CreateUserService:
    def __init__(self, create_user_repository: UserRepository) -> CreateUserResponseSchema:
        self.create_user_repository = create_user_repository

    def create_user(self, create_user_input: CreateUserInputSchema) -> CreateUserResponseSchema:
        return {"created": True}
