from typing import List

from sqlalchemy import ForeignKey
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


Base = declarative_base()


class Parent(Base):
    __tablename__ = "parent_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    children: Mapped[List["Child"]] = relationship(
        "Child",
        lazy="joined",
        uselist=False,
        back_populates="parent",
    )

    def __repr__(self) -> str:
        return f"<Parent (id, children) = ({self.id}, {self.children})>"


class Child(Base):
    __tablename__ = "child_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
    parent: Mapped["Parent"] = relationship(
        "Parent",
        lazy="joined",
        uselist=False,
        back_populates="children",
    )

    def __repr__(self) -> str:
        return f"<Child (id, parent) = ({self.id}, {self.parent.id})>"
