from api.cruds import auths as auth_api
from api.db import get_db
from api.schemas import auths as auth_schema
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/token", response_model=auth_schema.Auth)
def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth_api.find_user_with_auth(db, form_data.username)

    if not user:
        raise HTTPException(status_code=404, detail=f"Incorrect input data")

    hashed_password = auth_api.hash_password(form_data.password)

    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=404, detail=f"Incorrect input data")

    return {"access_token": user.name, "tokey_type": "bearer"}
