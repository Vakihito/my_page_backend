from fastapi import APIRouter
from src.goals.service import DeleteGoalsService
from src.goals.controller import DeleteGoalsController
from src.goals.infra import GoalsRepository
from src.shared.database_shared import get_db_session

db = next(get_db_session())


def delete_goals_router_factory() -> APIRouter:
    repository = GoalsRepository(db)
    service = DeleteGoalsService(repository)
    controller = DeleteGoalsController(service)
    return controller.router
