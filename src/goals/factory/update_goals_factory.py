from fastapi import APIRouter
from src.goals.service import UpdateGoalsService
from src.goals.controller import UpdateGoalsController
from src.goals.infra import GoalsRepository
from src.shared.database_shared import get_db_session

db = next(get_db_session())


def update_goals_router_factory() -> APIRouter:
    repository = GoalsRepository(db)
    service = UpdateGoalsService(repository)
    controller = UpdateGoalsController(service)
    return controller.router
