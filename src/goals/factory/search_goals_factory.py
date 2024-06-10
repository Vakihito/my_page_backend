from fastapi import APIRouter
from src.goals.service import SearchGoalsService
from src.goals.controller import SearchGoalsController
from src.goals.infra import GoalsRepository
from src.shared.database_shared import get_db_session

db = next(get_db_session())


def search_goals_router_factory() -> APIRouter:
    repository = GoalsRepository(db)
    service = SearchGoalsService(repository)
    controller = SearchGoalsController(service)
    return controller.router
