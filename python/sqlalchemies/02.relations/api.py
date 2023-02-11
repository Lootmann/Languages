from random import choice, randint
from string import ascii_uppercase

from sqlalchemy.orm import Session

from model import Post, User


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


def random_name() -> str:
    return choice(["hoge", "hage", "hige"]) + str(randint(100, 999))


def random_title_or_content() -> str:
    return choice([">>> ", "*** ", "### "]) + choice(ascii_uppercase) * 3


@title("INSERT")
def insert(db: Session):
    # create random users
    with db as DB:
        data = [{"name": random_name()} for _ in range(10)]
        DB.bulk_insert_mappings(User, data)
        DB.commit()

    # get all users
    user_count = db.query(User).count()

    with db as DB:
        data = [
            {
                "title": random_name(),
                "content": random_title_or_content(),
                "user_id": randint(0, user_count),
            }
            for _ in range(20)
        ]
        DB.bulk_insert_mappings(Post, data)
        DB.commit()


@title("select users")
def select_users(db: Session):
    for row in db.query(User.id, User.name).limit(5).all():
        print(row)


@title("select posts")
def select_posts(db: Session):
    for row in db.query(Post.id, Post.title, Post.content, Post.user_id).limit(5).all():
        print(row)


@title("select users with posts")
def select_join(db: Session):
    for r in db.query(User, Post).join(Post, User.id == Post.user_id).limit(5).all():
        user, post = r
        print(f"[{user.id}] {user.name} < [{post.id}] {post.title}: {post.content}")
