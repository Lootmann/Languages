from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    age: int
    address: str


class UserCreate(UserBase):
    pass


class UserCreateReponse(UserBase):
    id: int
