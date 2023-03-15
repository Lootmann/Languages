from typing import List, Optional

from sqlmodel import Field, Relationship, Session, SQLModel, create_engine


class Hero(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: Optional[str]
    password: str

    infos: List["Info"] = Relationship(back_populates="hero")


class Info(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str

    hero_id: Optional[int] = Field(default=None, foreign_key="hero.id")
    hero: Optional[Hero] = Relationship(back_populates="infos")


def main():
    engine = create_engine("sqlite:///dev.db")
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        hero = Hero(name="John Doe", email="johndoe@email.com", password="hogehoge")
        session.add(hero)
        session.commit()

        session.add(Info(title="hoge", hero_id=hero.id))
        session.add(Info(title="hage", hero_id=hero.id))
        session.add(Info(title="hige", hero_id=hero.id))
        session.commit()

    with Session(engine) as session:
        results = session.query(Hero).all()
        for res in results:
            print(res)

    with Session(engine) as session:
        results = session.query(Info).all()
        for res in results:
            print(res)


if __name__ == "__main__":
    main()
