from fastapi import APIRouter
from src.goals.service import GetByUserGoalsService
from src.goals.controller import GetByUserGoalsController
from src.goals.infra import GoalsRepository
from src.shared.database_shared import get_db_session

db = next(get_db_session())


def get_by_user_goals_router_factory() -> APIRouter:
    repository = GoalsRepository(db)
    service = GetByUserGoalsService(repository)
    controller = GetByUserGoalsController(service)
    return controller.router
