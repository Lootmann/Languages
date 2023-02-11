from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api import select_all, select_raw, select_where, insert_once, insert_bulk


def main():
    DATABASE_URL = "sqlite:///dev.db"
    engine = create_engine(DATABASE_URL, echo=True)

    Session = sessionmaker(bind=engine)
    db = Session()

    insert_once(db)
    insert_bulk(db)
    select_all(db)
    select_raw(db)
    select_where(db)
    db.close()


if __name__ == "__main__":
    main()
