from api import insert, select_join, select_posts, select_users
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    DATABASE_URL = "sqlite:///dev.db"
    engine = create_engine(DATABASE_URL, echo=True)

    session = sessionmaker(bind=engine)
    db = session()
    insert(db)
    select_users(db)
    select_posts(db)
    select_join(db)
    db.close()


if __name__ == "__main__":
    main()
