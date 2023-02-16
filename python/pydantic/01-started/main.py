from api import create_user, get_users
from db import DATABASE_URL
from schema import UserCreate
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    engine = create_engine(DATABASE_URL, echo=True)
    session = sessionmaker(bind=engine)

    db = session()

    data_from_api = {
        "id": 123,
        "name": "hoge",
        "age": 35,
        "sex": "male",
        "address": "here",
    }
    validation_data = UserCreate(**data_from_api)

    response = create_user(db, validation_data)
    print(">>> create_user : ", response)

    response = get_users(db)
    print(">>> response : ", response)

    db.close()


if __name__ == "__main__":
    main()
