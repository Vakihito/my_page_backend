from src.user.schema import CreateUserInputSchema, CreateUserResponseSchema

from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy.sql import func, literal_column
from starlette import status
from src.user.schema import CreateUserInputSchema, CreateUserResponseSchema
from src.user.model import UserModel
from loguru import logger
from src.main.exceptions import ApplicationException
from datetime import date, datetime


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, create_user_input: CreateUserInputSchema):
        new_user = UserModel(**create_user_input.model_dump())
        try:
            logger.info("create user ")
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)
        except IntegrityError:
            self.db.rollback()
            logger.info("error log")
            return None
        except SQLAlchemyError:
            self.db.rollback()
            raise ApplicationException(status_code=500, key="error doing something")
        finally:
            self.db.close()

        logger.info("create user")
        return None
