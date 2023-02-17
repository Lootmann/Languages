from api.cruds import auths as auth_api
from api.db import get_db
from api.models import users as user_model
from api.schemas import users as user_schema
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> user_schema.UserResponse:
    user = auth_api.decode_token(db, token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Authentication Credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


def get_current_active_user(
    current_user: user_schema.UserResponse = Depends(get_current_user),
) -> user_schema.UserResponse:
    return current_user


def hash_password(password: str) -> str:
    return f"fake_hash_{password}"


def decode_token(db: Session, username: str) -> user_schema.UserInDB:
    result: user_model.User | None = (
        db.query(user_model.User).filter(user_model.User.name == username).first()
    )
    if not result:
        return None

    user = user_schema.UserInDB(
        name=result.name,
        email=result.email,
        id=result.id,
        hashed_password=result.hashed_password,
    )

    return user


def find_user_with_auth(db: Session, user_name: str) -> user_model.User:
    return db.query(user_model.User).filter(user_model.User.name == user_name).first()
