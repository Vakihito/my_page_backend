from fastapi import APIRouter


class RoutersFactory:
    def __init__(self, routers, prefix: str, tags: list[str]):
        self.__routers = routers
        self.__prefix = prefix
        self.__tags = tags

    def get_all_routers(self) -> list[APIRouter]:
        return self.__routers

    def get_routers_prefix(self) -> str:
        return self.__prefix

    def get_routers_tags(self) -> list[str]:
        return self.__tags
