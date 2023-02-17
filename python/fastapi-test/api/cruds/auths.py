from api.models import users as user_model
from sqlalchemy.orm import Session


def hash_password(password: str) -> str:
    return f"fake_hash_{password}"


def find_user_with_auth(db: Session, user_name: str) -> user_model.User:
    return db.query(user_model.User).filter(user_model.User.name == user_name).first()
