import functools
from random import choice, randint, sample
from string import ascii_letters

from models import Like, Tweet, User
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select


def random_string(min_=5, max_=20) -> str:
    return "".join(sample(ascii_letters, randint(min_, max_)))


def title(msg: str):
    def wrapper(func):
        @functools.wraps(func)
        async def inner(*args, **kwargs):
            print("-----" * 5)
            print(f"--- {msg}")
            print("-----" * 5)
            await func(*args, **kwargs)
            print()

        return inner

    return wrapper


@title("Create User")
async def create_user(db: AsyncSession):
    user = User(name=random_string())
    db.add(user)
    await db.commit()
    await db.refresh(user)

    print(user)


@title("Show User")
async def select_user(db: AsyncSession):
    stmt = select(User)
    results = await db.execute(stmt)

    for r in results:
        print(r)
