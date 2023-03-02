from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship

Base = declarative_base()


class History(Base):
    __tablename__ = "histories"
    id: Mapped[int] = mapped_column(primary_key=True)

    # History : Talk = n : 1
    talks: Mapped[List["Talk"]] = relationship(back_populates="history")

    @staticmethod
    def create() -> "History":
        return History()

    def __repr__(self) -> str:
        return f"<History (id, talks) = ({self.id}, {self.talks})>"


class Talk(Base):
    __tablename__ = "talks"
    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int]

    # Talk : Sentence
    sentence: Mapped["Sentence"] = relationship(
        "Sentence",
        back_populates="talk",
        uselist=False,
    )

    # History : Talk = 1 : n
    history_id: Mapped[int] = mapped_column(ForeignKey("histories.id"))
    history: Mapped["History"] = relationship("History", back_populates="talks")

    @staticmethod
    def create(order_id: int, history: "History") -> "Talk":
        return Talk(order_id=order_id, history=history)

    def __repr__(self) -> str:
        return f"<Talk (id, order_id, sentence, history) = ({self.id}, {self.order_id}, {self.sentence}, {self.history.id})>"


class Sentence(Base):
    __tablename__ = "sentences"
    id: Mapped[int] = mapped_column(primary_key=True)

    sentence: Mapped[str]
    translation: Mapped[str]

    # Sentence : Talk = 1 : 1
    talk_id: Mapped[int] = mapped_column(ForeignKey("talks.id"), unique=True)
    talk: Mapped["Talk"] = relationship("Talk", back_populates="sentence")

    @staticmethod
    def create(talk: "Talk", s: str, t: str) -> "Sentence":
        return Sentence(talk=talk, sentence=s, translation=t)

    def __repr__(self) -> str:
        return f"<Sentence (id, sentence, translation, talk) = ({self.id}, {self.sentence}, {self.translation}, {self.talk.id})>"
