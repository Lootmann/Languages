from models import Like, Tweet, User
from sqlalchemy import create_engine

# dont need async when creating db
DB_URL = "sqlite:///dev.db"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    User.metadata.drop_all(bind=engine)
    User.metadata.create_all(bind=engine)

    Tweet.metadata.drop_all(bind=engine)
    Tweet.metadata.create_all(bind=engine)

    Like.metadata.drop_all(bind=engine)
    Like.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
