from src.goals.schema import SearchGoalsInputSchema, CreateGoalInputSchema
from src.goals.schema import DeleteGoalsInputSchema, DeleteGoalsResponseSchema
from src.goals.schema import CreateGoalInputSchema, UpdateGoalsResponseSchema
from sqlalchemy import and_, distinct, or_
from sqlalchemy import update as dbUpdate
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy.sql import func, literal_column
from starlette import status
from src.goals.schema import CreateGoalInputSchema, CreateGoalResponseSchema
from src.goals.model import GoalsModel
from loguru import logger
from src.main.exceptions import ApplicationException
from datetime import date, datetime


class GoalsRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_goal(self, create_goal_input: CreateGoalInputSchema):
        if isinstance(create_goal_input.start_date, str):
            create_goal_input.start_date = datetime.strptime(
                create_goal_input.start_date, "%Y-%m-%d"
            )
        if isinstance(create_goal_input.end_date, str):
            create_goal_input.end_date = datetime.strptime(
                create_goal_input.end_date, "%Y-%m-%d"
            )

        new_goal = GoalsModel(**create_goal_input.model_dump())
        try:
            logger.info("create new goal")
            self.db.add(new_goal)
            self.db.commit()
            self.db.refresh(new_goal)
        except IntegrityError:
            self.db.rollback()
            logger.info("goal duplicated, returning goal existent")
            return None
        except SQLAlchemyError:
            self.db.rollback()
            raise ApplicationException(
                status_code=500, key="postgres_keyword_error_to_create"
            )
        finally:
            self.db.close()

        logger.info("created new goal")

        return new_goal

    def update_goals(self, update_goals_input: CreateGoalInputSchema):
        update_goals_dict = {}
        for field, value in update_goals_input.__dict__.items():
            if (value is not None) and (field != "id"):
                update_goals_dict[field] = value
        stmt = (
            dbUpdate(GoalsModel)
            .where(GoalsModel.id == update_goals_input.id)
            .values(**update_goals_dict)
        )
        try:
            logger.info("update goals ")
            result = self.db.execute(stmt)
            self.db.flush()
            self.db.commit()

        except IntegrityError:
            self.db.rollback()
            logger.info("error log")
            return None
        except SQLAlchemyError as exc:
            logger.error(
                f"Error updating existing relation of goal on database: error = {exc}"
            )
            self.db.rollback()
            raise ApplicationException(status_code=500, key="error doing something")
        finally:
            self.db.close()

        logger.info("update goals")
        return result

    def delete_goals(self, delete_goals_input: DeleteGoalsInputSchema):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d")
        stmt = (
            dbUpdate(GoalsModel)
            .where(GoalsModel.id == delete_goals_input.id)
            .values(deleted_at=formatted_datetime)
        )
        try:
            logger.info("delete goals")
            self.db.execute(stmt)
            self.db.flush()
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            logger.info("error log")
            return None
        except SQLAlchemyError:
            self.db.rollback()
            raise ApplicationException(status_code=500, key="error doing something")
        finally:
            self.db.close()

        logger.info("delete goals")
        return None

    def delete_goals_hard(self, delete_goals_input: DeleteGoalsInputSchema):

        try:
            logger.info("delete goals hard")
            # first find the data to delete
            result = (
                self.db.query(GoalsModel)
                .filter(GoalsModel.id == delete_goals_input.id)
                .first()
            )
            self.db.delete(result)
            self.db.flush()
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            logger.info("error log")
            return None
        except SQLAlchemyError:
            self.db.rollback()
            raise ApplicationException(status_code=500, key="error doing something")
        finally:
            self.db.close()

        logger.info("delete goals hard")
        return None

    def search_goals(self, search_goals_input: SearchGoalsInputSchema):
        stm = or_(
            GoalsModel.title.like(f"%{search_goals_input.text_title}%"),
            GoalsModel.todo.like(f"%{search_goals_input.text_title}%"),
            GoalsModel.nottodo.like(f"%{search_goals_input.text_title}%"),
        )

        try:
            result = self.db.query(GoalsModel).filter(stm).all()
            logger.info("search goals ")
        except IntegrityError:
            self.db.rollback()
            logger.info("error log")
            return None
        except SQLAlchemyError:
            self.db.rollback()
            raise ApplicationException(status_code=500, key="error doing something")
        finally:
            self.db.close()

        logger.info("search goals")
        return result
