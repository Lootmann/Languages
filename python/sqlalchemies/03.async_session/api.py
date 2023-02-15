import functools
from random import choice, randint, sample
from string import ascii_uppercase

from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select

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
    return choice(["hoge", "hage", "hige"]) + str(randint(1000, 9999))


def random_title_or_content() -> str:
    return choice([">", "*", "#"]) * randint(1, 3) + "".join(sample(list(ascii_uppercase), 4))


@title("CREATE USER")
async def create_user(db: AsyncSession):
    db.add_all([User(name=random_name()) for _ in range(10)])
    await db.commit()


@title("CREATE POSTS")
async def create_posts(db: AsyncSession):
    result = await db.execute(select(User))
    user_num = len(result.all())

    db.add_all(
        [
            Post(
                title=random_title_or_content(),
                content=random_title_or_content(),
                user_id=randint(0, user_num),
            )
            for _ in range(10)
        ]
    )
    await db.commit()


@title("SELECT USERS")
async def get_all_users(db: AsyncSession):
    result = await db.execute(select(User.id, User.name).limit(5))
    for row in result:
        print(row)
    return result.all()


@title("SELECT POSTS")
async def get_all_posts(db: AsyncSession):
    result = await db.execute(select(Post.id, Post.title, Post.content, Post.user_id).limit(5))
    return result.all()


@title("SELECT USERS with POSTS")
async def select_join(db: AsyncSession):
    result = await db.execute(
        select(User, Post).join(Post, User.id == Post.user_id).order_by(User.id).limit(20)
    )
    for r in result.all():
        user, post = r
        print(f"[{user.id}] {user.name} < [{post.id}] {post.title}: {post.content}")


@title("UPDATE")
async def update(db: AsyncSession):
    """
    update random users and random posts
    """
    # update user
    res = (await db.execute(select(User).order_by(func.random()))).first()
    if not res:
        return

    user = res[0]
    user.name = "--- updated [:^) ---"

    db.add(user)
    await db.commit()
    await db.refresh(user)

    # update posts
    res = (await db.execute(select(Post).order_by(func.random()))).first()
    if not res:
        return

    post = res[0]

    post.title = "--- updated [:^) ---"
    post.content = "--- updated [:^) ---"

    db.add(post)
    await db.commit()
    await db.refresh(post)


@title("Find Updated Users and Posts")
async def find_updated(db: AsyncSession):
    results = await db.execute(
        select(User.id, User.name).filter(User.name == "--- updated [:^) ---")
    )
    for row in results.all():
        print(row)


@title("DELETE POST")
async def delete_user(db: AsyncSession):
    # get random user id
    user = (await db.execute(select(User).order_by(func.random()))).first()
    if not user:
        print("Empty User")
        return
    user_id = user[0].id

    # get all user's posts
    posts = (await db.execute(select(Post.id, Post.title).filter(Post.user_id == user_id))).all()

    if posts == []:
        print("No Post D:")
        return

    # delete all posts
    for post in posts:
        result = await db.get(Post, post.id)

        if not result:
            return

        await db.delete(result)
        await db.commit()

    # delete user
    user = await db.get(User, user_id)

    if not user:
        return

    await db.delete(user)
    await db.commit()
