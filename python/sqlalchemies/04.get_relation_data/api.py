import functools
from random import randint

from model import Child, Parent
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select


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


@title("CREATE Parent")
async def create_parents(db: AsyncSession):
    db.add_all([Parent() for _ in range(10)])
    await db.commit()


@title("CREATE Children")
async def create_children(db: AsyncSession):
    for _ in range(20):
        parent = (await db.execute(select(Parent).order_by(func.random()))).first()
        if not parent:
            print("no parent")
            continue

        child = Child(parent_id=parent[0].id)
        db.add(child)
        await db.commit()


@title("SELECT Parents")
async def get_all_parents(db: AsyncSession):
    results = await db.execute(select(Parent))

    for r in results.all():
        print(r)

    return results


@title("SELECT Parent")
async def get_all_parent(db: AsyncSession):
    results = await db.execute(select(Parent))

    for r in results.all():
        parent, child = r
        print(parent, child)

    return results


@title("SELECT Parent with Children")
async def get_all_children(db: AsyncSession):
    result = (await db.execute(select(Parent).filter_by(id=6))).first()

    if not result:
        return

    print(result[0].children)

    return result
