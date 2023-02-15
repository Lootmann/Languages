from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship


class RepresentableBase(object):
    def __repr__(self):
        """Dump all columns and value automagically.

        This code is copied a lot from followings.
        See also:
           - https://gist.github.com/exhuma/5935162#file-representable_base-py
           - http://stackoverflow.com/a/15929677
           - https://gene.hatenablog.com/entry/20151011/1444546659
        """
        #: Columns.
        columns = ", ".join(
            [
                "{0}={1}".format(k, repr(self.__dict__[k]))
                for k in self.__dict__.keys()
                if k[0] != "_"
            ]
        )

        return "<{0}({1})>".format(self.__class__.__name__, columns)


Base = declarative_base(cls=RepresentableBase)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    posts: Mapped["Post"] = relationship(back_populates="user")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)

    # foreign key
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="posts")
