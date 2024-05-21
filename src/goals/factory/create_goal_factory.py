from fastapi import APIRouter
from src.goals.service import CreateGoalService
from src.goals.controller import CreateGoalController


def create_goal_router_factory() -> APIRouter:
    service = CreateGoalService()
    controller = CreateGoalController(service)
    return controller.router
