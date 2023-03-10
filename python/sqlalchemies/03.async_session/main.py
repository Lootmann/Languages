import asyncio

from api import (
    create_posts,
    create_user,
    delete_user,
    find_updated,
    get_all_posts,
    get_all_users,
    select_join,
    update,
)
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


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
    await update(db)
    await find_updated(db)
    await delete_user(db)

    await db.close()


if __name__ == "__main__":
    asyncio.run(main())
