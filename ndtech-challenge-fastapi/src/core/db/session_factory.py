from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_scoped_session
)
from sqlalchemy.orm import sessionmaker
from logging import getLogger
from src.core.constants import (
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_NAME
)
from asyncio import current_task

logger = getLogger()


class SessionFactory:
    """This is a simple implementation of the sqlalchemy engine that allows
    for communicating with the db.

    It should also allow for dependency injection

    Args:
        db_url: Full url of the db
    """
    def __init__(self, db_url: str, **kwargs) -> None:
        self.engine = create_async_engine(db_url, pool_pre_ping=True, **kwargs)
        self.factory = sessionmaker(
            class_=AsyncSession,
            expire_on_commit=False,
            bind=self.engine
        )

    async def __aenter__(self) -> AsyncSession:
        self.session = async_scoped_session(
            self.factory, scopefunc=current_task)
        return self.session

    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        await self.session.close()
        if exc_type:
            logger.error(f"Session closed with exception: {exc_value}")


# I used the singleton pattern to instantiate this once otherwise issues arise
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}" # noqa
session_factory = SessionFactory(DATABASE_URL)
