from typing import List

from api.cruds import users as user_api
from api.db import get_db
from api.schemas import users as user_schema
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/{user_id}", response_model=user_schema.UserReponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = user_api.find_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User:{user_id} Not Found")
    return user


@router.get("/", response_model=List[user_schema.UserReponse])
def get_all_users(db: Session = Depends(get_db)):
    return user_api.get_all_users(db)


@router.post("/", response_model=user_schema.UserCreateResponse)
def create_user(user_body: user_schema.UserCreate, db: Session = Depends(get_db)):
    return user_api.create_user(db, user_body)
