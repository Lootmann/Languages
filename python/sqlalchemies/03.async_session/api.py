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
    return choice([">", "*", "#"]) * randint(1, 3) + "".join(
        sample(list(ascii_uppercase), 4)
    )


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
    result = await (
        db.execute(
            select(Post.id, Post.title, Post.content, Post.user_id).limit(5)
        )
    )
    return result.all()


@title("select users with posts")
async def select_join(db: AsyncSession):
    result = await (
        db.execute(
            select(User, Post)
            .join(Post, User.id == Post.user_id)
            .order_by(User.id)
            .limit(20)
        )
    )
    for r in result.all():
        user, post = r
        print(
            f"[{user.id}] {user.name} < [{post.id}] {post.title}: {post.content}"
        )


@title("UPDATE")
async def update(db: AsyncSession):
    """
    update random users and random posts
    """
    # update user
    user_num = await (db.scalar(select(func.count()).select_from(User)))

    user: User | None = (
        await db.execute(select(User).filter(User.id == randint(0, user_num)))
    ).first()  # type: ignore

    if not user:
        return

    user[0].name = "updated :^)"
    db.add(user[0])
    await db.commit()
    await db.refresh(user[0])

    # update posts
    post_num = await (db.scalar(select(func.count()).select_from(Post)))

    post: Post | None = (
        await db.execute(select(Post).filter(Post.id == randint(0, post_num)))
    ).first()  # type: ignore

    if not post:
        return

    post[0].title = "updated :^)"
    post[0].content = "updated :^)"

    db.add(post[0])
    await db.commit()
    await db.refresh(post[0])


@title("Find Updated Users and Posts")
async def find_updated(db: AsyncSession):
    results = await db.execute(
        select(User.id, User.name).filter(User.name == "updated :^)")
    )
    for row in results.all():
        print(row)


@title("DELETE POST")
async def delete_user(db: AsyncSession):
    # get one
    user_count = await (db.scalar(select(func.count()).select_from(User)))
    user_id = randint(0, user_count)

    posts = (
        await db.execute(
            select(Post.id, Post.title).filter(Post.user_id == user_id)
        )
    ).all()

    if posts == []:
        return

    for post in posts:
        result = (
            await db.execute(select(Post).where(Post.id == post.id))
        ).first()

        if not result:
            return

        await db.delete(result[0])
        await db.commit()

    user = (await db.execute(select(User).filter(User.id == user_id))).first()

    if not user:
        return

    await db.delete(user[0])
    await db.commit()
