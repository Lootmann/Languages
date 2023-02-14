from typing import List

from pydantic import BaseModel, Field, validator

import post


class UserBase(BaseModel):
    id: int
    age: int
    name: str

    class Config:
        orm_mode = True

    @validator("age")
    def age_must_between_0_to_120(cls, age_):
        if 0 <= age_ <= 120:
            return age_
        raise ValueError("Field.Age must between 0 to 120")


class User(UserBase):
    posts: List[post.PostBase] = Field(None)
