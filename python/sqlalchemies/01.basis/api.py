from model import User
from sqlalchemy import between, insert, select
from sqlalchemy.orm import Session
from sqlalchemy.sql import text


def title(msg: str):
    def wrapper(func):
        def inner(*args, **kwargs):
            print("-----" * 10)
            print(f"--- {msg}")
            print("-----" * 10)
            func(*args, **kwargs)
            print()

        return inner

    return wrapper


@title("insert once record")
def insert_once(db: Session):
    db.execute(insert(User), {"name": "once"})


@title("insert many records at once")
def insert_bulk(db: Session):
    db.execute(
        insert(User),
        [
            {"name": "hoge"},
            {"name": "hage"},
            {"name": "hige"},
            {"name": "moge"},
            {"name": "mage"},
            {"name": "mige"},
        ],
    )
    db.commit()


@title("SELECT ALL")
def select_all(db: Session):
    # now show all records, only shows 20 records
    stmt = select(User.id, User.name)
    for idx, row in enumerate(db.execute(stmt).all()):
        if idx >= 20:
            break
        print(idx, row)


@title("SELECT USING RAW SQL")
def select_raw(db: Session):
    stmt = text("SELECT * FROM users WHERE id BETWEEN 5 AND 10")
    for row in db.execute(stmt).all():
        print(row)


@title("SELECT + WHERE, LIMIT, BETWEEN ...")
def select_where(db: Session):
    """WHERE
    SELECT users.id, users.name
    FROM users
    WHERE users.id = ?
    """
    stmt = select(User).filter(User.id == 3)
    for row in db.execute(stmt).all():
        print(row)

    """BETWEEN
    SELECT users.id, users.name
    FROM users
    WHERE users.id BETWEEN ? AND ? + (5, 10)
    """
    stmt = select(User.id, User.name).where(between(User.id, 5, 10))
    for row in db.execute(stmt).all():
        print(row)
