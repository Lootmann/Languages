from db import DATABASE_URL
from model import Base
from sqlalchemy import create_engine

engine = create_engine(DATABASE_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
