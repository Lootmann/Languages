import functools
from random import choice, randint
from sqlalchemy.sql import select
from sqlalchemy.ext.asyncio import AsyncSession
from string import ascii_uppercase
from model import Post, User


def title(msg: str):
    def wrapper(func):
        @functools.wraps(func)
        async def inner(*args, **kwargs):
            print("-----" * 10)
            print(f"--- {msg}")
            print("-----" * 10)
            await func(*args, **kwargs)
            print()

        return inner

    return wrapper


def random_name() -> str:
    return choice(["hoge", "hage", "hige"]) + str(randint(100, 999))


def random_title_or_content() -> str:
    return choice([">>> ", "*** ", "### "]) + choice(ascii_uppercase) * 3


@title("CREATE USER")
async def create_user(db: AsyncSession):
    db.add_all([User(name=random_name()) for _ in range(10)])
    await db.commit()


@title("CREATE POSTS")
async def create_posts(db: AsyncSession):
    result = await (db.execute(select(User)))
    user_num = len(result.all())

    db.add_all(
        [
            Post(
                title=random_title_or_content(),
                content=random_title_or_content(),
                user_id=randint(0, user_num),
            )
            for _ in range(20)
        ]
    )
    await db.commit()


@title("SELECT USERS")
async def get_all_users(db: AsyncSession):
    result = await (db.execute(select(User.id, User.name).limit(5)))
    return result.all()


@title("SELECT POSTS")
async def get_all_posts(db: AsyncSession):
    result = await (db.execute(select(Post.id, Post.title, Post.content, Post.user_id).limit(5)))
    return result.all()


@title("select users with posts")
async def select_join(db: AsyncSession):
    result = await (
        db.execute(
            select(User, Post).join(Post, User.id == Post.user_id).order_by(User.id).limit(20)
        )
    )
    for r in result.all():
        user, post = r
        print(f"[{user.id}] {user.name} < [{post.id}] {post.title}: {post.content}")
