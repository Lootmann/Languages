from pydantic import BaseModel


class UserBase(BaseModel):
    name: str = "username"
    email: str = "email"

    class Config:
        orm_mode = True


class UserResponse(UserBase):
    id: int


class UserCreate(UserBase):
    # NOTE: convert password to hashed password when insert into db
    password: str = "password"


class UserCreateResponse(UserBase):
    id: int


class UserInDB(UserBase):
    id: int
    hashed_password: str
