from models import History, Sentence, Talk
from sqlalchemy import create_engine

# dont need async when creating db
DB_URL = "sqlite:///dev.db"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    History.metadata.drop_all(bind=engine)
    History.metadata.create_all(bind=engine)

    Sentence.metadata.drop_all(bind=engine)
    Sentence.metadata.create_all(bind=engine)

    Talk.metadata.drop_all(bind=engine)
    Talk.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
