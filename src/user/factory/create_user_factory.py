from fastapi import APIRouter
from src.user.service import CreateUserService
from src.user.controller import CreateUserController
from src.user.infra import UserRepository
from src.shared.database_shared import get_db_session

db = next(get_db_session())


def create_user_router_factory() -> APIRouter:
    repository = UserRepository(db)
    service = CreateUserService(repository)
    controller = CreateUserController(service)
    return controller.router
