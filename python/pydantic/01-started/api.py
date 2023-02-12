from typing import List

from sqlalchemy.orm import Session

from model import User as user_model
from schema import UserCreate, UserCreateReponse


def create_user(db: Session, user_schema: UserCreate) -> UserCreateReponse:
    user = user_model(**user_schema.dict())
    db.add(user)
    db.commit()
    return user


def get_users(db: Session) -> List[UserCreateReponse]:
    return db.query(user_model).all()
