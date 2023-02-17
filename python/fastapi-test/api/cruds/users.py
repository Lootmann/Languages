from typing import List

from api.cruds import auths as auth_api
from api.models import users as user_model
from api.schemas import users as user_schame
from sqlalchemy.orm import Session


def get_all_users(db: Session) -> List[user_model.User]:
    return db.query(user_model.User).all()


def find_user_by_id(db: Session, user_id: int) -> user_model.User | None:
    return db.get(user_model.User, user_id)


def find_user_by_name(db: Session, user_name: str) -> user_model.User | None:
    return db.query(user_model.User).filter(user_model.User.name == user_name).first()


def create_user(db: Session, user_body: user_schame.UserCreate) -> user_model.User:
    insert_user = user_model.User()

    insert_user.name = user_body.name
    insert_user.email = user_body.email
    insert_user.hashed_password = auth_api.hash_password(user_body.password)

    db.add(insert_user)
    db.commit()
    db.refresh(insert_user)

    return insert_user
