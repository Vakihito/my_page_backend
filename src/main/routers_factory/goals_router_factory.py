import src.goals.factory as goals_factory
from src.main.routers_factory.routers_factory import RoutersFactory

routers = [
    goals_factory.search_goals_router_factory(),
    goals_factory.delete_goals_router_factory(),
    goals_factory.update_goals_router_factory(),
    goals_factory.create_goal_router_factory(),
]


class GoalsRouterFactory(RoutersFactory):
    def __init__(self) -> None:
        super().__init__(routers, prefix="/goal", tags=["Goal"])
