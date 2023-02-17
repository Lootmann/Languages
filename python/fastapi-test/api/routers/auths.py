from datetime import timedelta

from api.cruds import auths as auth_api
from api.db import get_db
from api.schemas import auths as auth_schema
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/token", response_model=auth_schema.Token)
def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth_api.authenticate_user(db, form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=404,
            detail=f"Incorrect input data",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=auth_api.ACCESS_TOKEN_EXPIRE_MINUTES)

    data = {"sub": user.name}
    access_token = auth_api.create_access_token(data, access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}
