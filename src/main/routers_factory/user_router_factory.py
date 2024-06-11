import src.user.factory as user_factory
from src.main.routers_factory.routers_factory import RoutersFactory

routers = [
    user_factory.create_user_router_factory(),
]


class UserRouterFactory(RoutersFactory):
    def __init__(self) -> None:
        super().__init__(routers, prefix="/user", tags=["User"])
