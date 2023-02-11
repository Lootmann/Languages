import asyncio
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from api import create_user, get_all_users, create_posts, get_all_posts, select_join


async def main():
    DATABASE_URL = "sqlite+aiosqlite:///dev.db"
    async_engine = create_async_engine(DATABASE_URL, echo=True)
    session = sessionmaker(
        bind=async_engine,
        autocommit=False,
        autoflush=False,
        class_=AsyncSession,
    )

    db = session()

    await create_user(db)
    await create_posts(db)
    await get_all_users(db)
    await get_all_posts(db)
    await select_join(db)

    await db.close()


if __name__ == "__main__":
    asyncio.run(main())
