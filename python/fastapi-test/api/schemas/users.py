from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class UserReponse(UserBase):
    id: int


class UserCreate(UserBase):
    # NOTE: convert password to hashed password when insert into db
    password: str


class UserCreateResponse(UserBase):
    id: int


class UserInDB(UserBase):
    id: int
    hashed_password: str
