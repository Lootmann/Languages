from sqlalchemy import create_engine

from api.db import DATABASE_URL
from api.models.users import User

engine = create_engine(DATABASE_URL, echo=True)


def reset_database():
    User.metadata.drop_all(bind=engine)
    User.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
