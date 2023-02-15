from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    posts: Mapped["Post"] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"<User (id, name, posts) = ({self.id}, {self.name}, {self.posts})>"


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)

    # foreign key
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="posts")

    def __repr__(self) -> str:
        return f"<Post (id, ti, co) = ({self.id}, {self.title}, {self.content}, {self.user_id})>"
