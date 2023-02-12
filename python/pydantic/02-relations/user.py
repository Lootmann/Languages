from typing import List

from pydantic import BaseModel, Field

import post


class UserBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class User(UserBase):
    posts: List[post.PostBase] = Field(None)
