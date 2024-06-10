from fastapi import APIRouter
from src.goals.service import CreateGoalService
from src.goals.controller import CreateGoalController
from src.goals.infra import GoalsRepository
from src.shared.database_shared import get_db_session

db = next(get_db_session())


def create_goal_router_factory() -> APIRouter:
    repository = GoalsRepository(db)
    service = CreateGoalService(repository)
    controller = CreateGoalController(service)
    return controller.router
