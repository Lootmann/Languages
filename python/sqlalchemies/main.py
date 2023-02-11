from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import User


def main():
    DATABASE_URL = "sqlite:///dev.db"
    engine = create_engine(DATABASE_URL, echo=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Insert
    user = User()
    user.name = "hoge"

    # read all User
    for r in session.query(User):
        print(r.id, r.name)

    session.add(user)
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
