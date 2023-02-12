from pydantic import BaseModel, Field


class PostBase(BaseModel):
    id: int
    title: str = Field("")
    content: str = Field("")

    class Config:
        orm_mode = True


class Post(PostBase):
    pass
