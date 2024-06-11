from src.user.service import CreateUserService
from src.user.schema import CreateUserInputSchema, CreateUserResponseSchema
from starlette import status
from fastapi import APIRouter, Body, Depends


class CreateUserController:
    def __init__(self, create_user_service: CreateUserService):
        self.create_user_service = create_user_service
        self.router = APIRouter()
        self.router.add_api_route(
            "/create_user",
            self.handle,
            methods=["POST"],
            status_code=status.HTTP_201_CREATED,
            response_model=CreateUserResponseSchema,
            name="",
        )

    async def handle(self, create_user_input: CreateUserInputSchema):
        return self.create_user_service.create_user(create_user_input)
