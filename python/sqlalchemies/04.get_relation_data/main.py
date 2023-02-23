import asyncio

from api import create_children, create_parents, get_all_children, get_all_parents
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

    # await create_parents(db)
    # await create_children(db)
    await get_all_parents(db)
    await get_all_children(db)

    await db.close()


if __name__ == "__main__":
    asyncio.run(main())
