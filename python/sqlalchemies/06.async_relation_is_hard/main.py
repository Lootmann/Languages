from random import randint

from models import History, Sentence, Talk
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session, sessionmaker

DB_URL = "sqlite:///dev.db"
engine = create_engine(DB_URL, echo=False)
session = sessionmaker(bind=engine)


def get_all_talks(history_id: int, db: Session):
    return db.query(Talk.order_id).where(Talk.history_id == history_id).all()


def get_max_order_id(history_id: int, db: Session) -> int:
    print("_max_order")
    talk_order_ids = db.query(Talk.order_id).where(Talk.history_id == history_id).all()
    orders = [0]
    for talk in talk_order_ids:
        orders.append(talk[0])
    return max(orders)


def get_random_history(db: Session):
    res = db.query(History).order_by(func.random()).first()
    return res


def get_hisotry(history_id: int, db: Session):
    res = db.query(History).where(History.id == history_id).first()
    return res


def main():
    print("\n***" * 3)
    with session() as db:
        # create sentence
        for _ in range(1):
            h = History.create()
            db.add(h)
            db.commit()
            db.refresh(h)

        # get random history
        history_id = get_random_history(db).id

        for _ in range(randint(5, 10)):
            # get history
            history = get_hisotry(history_id, db)

            # get max order id
            max_order_id = get_max_order_id(history_id, db)

            # create Talk
            t = Talk.create(order_id=max_order_id + 1, history=history)

            # create sentence
            s = Sentence.create(t, "hoge", "hage")

            db.add(t)
            db.add(s)

            history.talks.append(t)
            db.commit()

    print("\n***" * 3)
    with session() as db:
        print(">>>")
        print(">>> histories")
        print(">>>")
        histories = db.query(History).all()

        for h in histories:
            print("-----" * 10)
            print(h)
            print("---")
            for talk in h.talks:
                print(talk)

        # print(">>> Talks")
        # talks = db.query(Talk).all()
        # for t in talks:
        #     print(t)
        #
        # print(">>> Sentences")
        # sentences = db.query(Sentence).all()
        # for s in sentences:
        #     print(s)
        #


if __name__ == "__main__":
    main()
