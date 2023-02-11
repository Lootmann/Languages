from sqlalchemy import select, insert, between
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from model import User


def insert_once(db: Session):
    db.execute(insert(User), {"name": "once"})


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


def select_all(db: Session):
    stmt = select(User.id, User.name)
    for idx, row in enumerate(db.execute(stmt).all()):
        print(idx, row)


def select_raw(db: Session):
    stmt = text("SELECT * FROM users WHERE id BETWEEN 5 AND 10")
    for row in db.execute(stmt).all():
        print(row)


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
