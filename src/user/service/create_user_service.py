from src.user.schema import CreateUserInputSchema, CreateUserResponseSchema
from src.user.model import UserModel
from src.user.infra import UserRepository
from uuid import uuid4


class CreateUserService:
    def __init__(self, create_user_repository: UserRepository) -> CreateUserResponseSchema:
        self.create_user_repository = create_user_repository

    def create_user(self, create_user_input: CreateUserInputSchema) -> CreateUserResponseSchema:
        if create_user_input.id is None:
            create_user_input.id = uuid4()

        self.create_user_repository.create_user(create_user_input)
        return {"created": True}
