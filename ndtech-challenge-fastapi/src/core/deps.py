from src.core.db.session_factory import session_factory


async def get_db_session():
    async with session_factory as session:
        yield session
