import os
import sys

print(f"sys.argv : {sys.argv}")
for i, arg in enumerate(sys.argv):
    if i == 1:
        main_service = arg  # "goals"
    if i == 2:
        service_name = arg  # "update"
main_folder = f"/workspace/src/{main_service}"

model_name = main_folder.split("/")[-1]
service_name = f"{service_name}_{model_name}"
main_service_cap = main_service.capitalize()

pathing_name = ".".join(main_folder.split("/")[2:])
pathing_name_src = ".".join(main_folder.split("/")[2:-1])

print(f"creatting new {service_name}")


def create_folder(cur_path):
    if not os.path.exists(cur_path):
        os.mkdir(cur_path)


def ext(cur_path):
    return os.path.exists(cur_path)


def create_file(cur_file_path):
    with open(cur_file_path, "w+") as f:
        f.write("")


def write_new_file(cur_file_path, new_data):
    with open(cur_file_path, "w+") as f:
        f.write(new_data)


def write_new_file_a(cur_file_path, new_data):
    with open(cur_file_path, "a") as f:
        f.write(f"\n{new_data}")


def update_file(cur_file_path, news_str):
    with open(cur_file_path, "a") as f:
        f.write(news_str)


def add_name_to_init(init_path, file_name, object_name):
    new_import = f"from .{file_name} import {object_name}\n"
    update_file(init_path, new_import)


def case_string(s):
    words = s.split("_")
    transformed = "".join(word.capitalize() for word in words)
    return transformed


def add_new_import(cur_file, new_import_data):
    updated_file_data = ""
    with open(cur_file, "r") as f:
        file_data = f.read()
        updated_file_data = f"{new_import_data}\n{file_data}"
    with open(cur_file, "w+") as f:
        f.write(updated_file_data)


def is_file_empty(cur_file):
    file_data = ""
    with open(cur_file, "r") as f:
        file_data = f.read()
    if len(file_data) == 0:
        return True
    return False


service_cased = case_string(service_name)

if not os.path.exists(main_folder):
    create_folder(f"{main_folder}/controller")
    create_file(f"{main_folder}/controller/__init__.py")

    create_folder(f"{main_folder}/factory")
    create_file(f"{main_folder}/factory/__init__.py")

    create_folder(f"{main_folder}/infra")
    create_file(f"{main_folder}/infra/__init__.py")
    create_file(f"{main_folder}/infra/{main_service}.py")

    create_folder(f"{main_folder}/model")
    create_file(f"{main_folder}/model/__init__.py")
    create_file(f"{main_folder}/model/{main_service}.py")

    create_folder(f"{main_folder}/schema")
    create_file(f"{main_folder}/schema/__init__.py")
    create_folder(f"{main_folder}/service")
    create_file(f"{main_folder}/service/__init__.py")

    create_file(
        f"/workspace/src/main/routers_factory/{main_service}_router_factory.py"
    )

########################
## create crontroller ##
########################
controller_file_content = f"""from {pathing_name}.service import {service_cased}Service
from {pathing_name}.schema import {service_cased}InputSchema, {service_cased}ResponseSchema
from starlette import status
from fastapi import APIRouter, Body, Depends


class {service_cased}Controller:
    def __init__(self, {service_name}_service: {service_cased}Service):
        self.{service_name}_service = {service_name}_service
        self.router = APIRouter()
        self.router.add_api_route(
            "/{service_name}",
            self.handle,
            methods=["POST"],
            status_code=status.HTTP_201_CREATED,
            response_model={service_cased}ResponseSchema,
            name="",
        )

    async def handle(self, {service_name}_input: {service_cased}InputSchema):
        return self.{service_name}_service.{service_name}({service_name}_input)
"""

write_new_file(
    f"{main_folder}/controller/{service_name}_controller.py", controller_file_content
)
add_name_to_init(
    f"{main_folder}/controller/__init__.py",
    f"{service_name}_controller",
    f"{service_cased}Controller",
)

####################
## create factory ##
####################
factory_file_content = f"""from fastapi import APIRouter
from {pathing_name}.service import {service_cased}Service
from {pathing_name}.controller import {service_cased}Controller
from {pathing_name}.infra import {main_service_cap}Repository
from {pathing_name_src}.shared.database_shared import get_db_session

db = next(get_db_session())


def {service_name}_router_factory() -> APIRouter:
    repository = {main_service_cap}Repository(db)
    service = {service_cased}Service(repository)
    controller = {service_cased}Controller(service)
    return controller.router
"""

write_new_file(f"{main_folder}/factory/{service_name}_factory.py", factory_file_content)
add_name_to_init(
    f"{main_folder}/factory/__init__.py",
    f"{service_name}_factory",
    f"{service_name}_router_factory",
)

##################
## create infra ##
##################
if is_file_empty(f"{main_folder}/infra/{main_service}.py"):
    factory_file_content_init = f"""from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy.sql import func, literal_column
from starlette import status
from {pathing_name}.schema import {service_cased}InputSchema, {service_cased}ResponseSchema
from {pathing_name}.model import {main_service_cap}Model
from loguru import logger
from {pathing_name_src}.main.exceptions import ApplicationException
from datetime import date, datetime


class {main_service_cap}Repository:
    def __init__(self, db: Session):
        self.db = db
"""
    write_new_file_a(
        f"{main_folder}/infra/{main_service}.py", factory_file_content_init
    )
    add_name_to_init(
        f"{main_folder}/infra/__init__.py",
        f"{main_service}",
        f"{main_service_cap}Repository",
    )

factory_file_content = f"""
    def {service_name}(self, {service_name}_input: {service_cased}InputSchema):
        try:
            logger.info("{' '.join(service_name.split('_'))} ")
        except IntegrityError:
            self.db.rollback()
            logger.info("error log")
            return None
        except SQLAlchemyError:
            self.db.rollback()
            raise ApplicationException(
                status_code=500, key="error doing something"
            )
        finally:
            self.db.close()

        logger.info("{' '.join(service_name.split('_'))}")
        return None
"""

write_new_file_a(f"{main_folder}/infra/{main_service}.py", factory_file_content)
add_new_import(
    f"{main_folder}/infra/{main_service}.py",
    f"from {pathing_name}.schema import {service_cased}InputSchema, {service_cased}ResponseSchema",
)


##################
## create model ##
##################
if is_file_empty(f"{main_folder}/model/{main_service}.py"):
    model_file_content_init = f"""from {pathing_name_src}.shared.database_shared import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import (
    Column,
    String,
    DateTime,
    text,
)


class {main_service_cap}Model(Base):
    __tablename__ = "{main_service}"
"""
    write_new_file(f"{main_folder}/model/{main_service}.py", model_file_content_init)

##################
## create schema ##
##################
if is_file_empty(f"{main_folder}/schema/{main_service}.py"):
    model_file_content_init = f"""from uuid import UUID
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict
"""
    write_new_file(f"{main_folder}/schema/{main_service}.py", model_file_content_init)


schema_file_content = f"""
class {service_cased}InputSchema(BaseModel):
    some_data: bool

class {service_cased}ResponseSchema(BaseModel):
    created: bool

"""

write_new_file_a(f"{main_folder}/schema/{main_service}.py", schema_file_content)
add_name_to_init(
    f"{main_folder}/schema/__init__.py",
    f"{main_service}",
    f"({service_cased}InputSchema, {service_cased}ResponseSchema)",
)

##################
## create service ##
##################
return_dict = {"created": True}

service_file_content = f"""from {pathing_name}.schema import {service_cased}InputSchema, {service_cased}ResponseSchema
from {pathing_name}.model import GoalsModel
from {pathing_name}.infra import GoalsRepository


class {service_cased}Service:
    def __init__(
        self, {service_name}_repository: GoalsRepository
    ) -> {service_cased}ResponseSchema:
        self.{service_name}_repository = {service_name}_repository

    def {service_name}(
        self, {service_name}_input: {service_cased}InputSchema
    ) -> {service_cased}ResponseSchema:
        return {return_dict}
"""
write_new_file(f"{main_folder}/service/{service_name}_service.py", service_file_content)
add_name_to_init(
    f"{main_folder}/service/__init__.py",
    f"{service_name}_service",
    f"{service_cased}Service",
)

##########################
## add new route factory ##
##########################
router_file = (
    f"/workspace/src/main/routers_factory/{main_service}_router_factory.py"
)
if is_file_empty(router_file):
    model_file_content_init = f"""import {pathing_name}.factory as {main_service}_factory
from {pathing_name_src}.main.routers_factory.routers_factory import RoutersFactory

routers = [
    {main_service}_factory.{service_name}_router_factory(),
]

class {main_service_cap}RouterFactory(RoutersFactory):
    def __init__(self) -> None:
        super().__init__(routers, prefix="/{main_service}", tags=["{main_service_cap}"])
"""
    write_new_file(
        router_file,
        model_file_content_init,
    )
else:
    with open(router_file, "r") as f:
        read_router_file = f.read()
    routers = read_router_file.split("routers = [")
    new_routing = f"{routers[0]}routers = [{main_service}_factory.{service_name}_router_factory(), {routers[1]}"
    write_new_file(
        router_file,
        new_routing,
    )
