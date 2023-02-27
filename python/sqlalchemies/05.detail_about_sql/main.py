import asyncio

import api
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

DATABASE_URL = "sqlite+aiosqlite:///dev.db"
async_engine = create_async_engine(DATABASE_URL, echo=True)

session = async_sessionmaker(
    bind=async_engine,
    autocommit=False,
    autoflush=False,
    class_=AsyncSession,
)


def title(msg: str):
    print("******" * 10)
    print("***", msg)
    print("******" * 10)


async def main():
    async with session() as db:
        await api.create_user(db)
        await api.create_tweet(db)
        await api.create_like(db)

    async with session() as db:
        await api.select_user(db)
        await api.select_tweet(db)

    async with session() as db:
        await api.test(db)


if __name__ == "__main__":
    asyncio.run(main())
