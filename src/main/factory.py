from fastapi import APIRouter, FastAPI
from src.main.routers_factory import *
from src.main.routers_factory.routers_factory import RoutersFactory

from fastapi import APIRouter


def include_multiple_routers(routers: list[APIRouter], prefix: str, tags: list[str], app: FastAPI):
    for router in routers:
        app.include_router(router=router, prefix=prefix, tags=tags)


def include_routers_from_multiple_factories_into_app(app: FastAPI, factories: list[RoutersFactory]):
    for factory_router in factories:
        routers = factory_router.get_all_routers()
        prefix = factory_router.get_routers_prefix()
        tags = factory_router.get_routers_tags()
        include_multiple_routers(app=app, routers=routers, prefix=prefix, tags=tags)


def setup_router_factories(app: FastAPI):
    goals_router_factory = GoalsRouterFactory()
    routers_factories: list[RoutersFactory] = [goals_router_factory]

    include_routers_from_multiple_factories_into_app(app=app, factories=routers_factories)

    return app
