"""
A User has Many Tweets
A Tweet has Many Likes
A User Has Many Likes

User  : Tweet = 1 : n
Tweet : Like  = 1 : n
User  : Like  = 1 : n
"""

from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    """
    CREATE TABLE users (
            id INTEGER NOT NULL,
            PRIMARY KEY (id)
    );
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    tweets: Mapped[List["Tweet"]] = relationship("Tweet", back_populates="user")
    likes: Mapped[List["Like"]] = relationship("Like", back_populates="user")

    def __repr__(self) -> str:
        return f"<User {self.id}>"


class Tweet(Base):
    """
    CREATE TABLE tweets (
        id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(user_id) REFERENCES users (id)
    );
    """

    __tablename__ = "tweets"

    id: Mapped[int] = mapped_column(primary_key=True)
    message: Mapped[str]

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="tweets")

    likes: Mapped[List["Like"]] = relationship("Like", back_populates="tweet")

    def __repr__(self) -> str:
        return f"<Tweet {self.id}>"


class Like(Base):
    """
    CREATE TABLE likes (
        id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        tweet_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(user_id) REFERENCES users (id),
        FOREIGN KEY(tweet_id) REFERENCES tweets (id)
    );
    """

    __tablename__ = "likes"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="likes")

    tweet_id: Mapped[int] = mapped_column(ForeignKey("tweets.id"))
    tweet: Mapped["Tweet"] = relationship("Tweet", back_populates="likes")

    def __repr__(self) -> str:
        return f"<Like {self.id}>"
