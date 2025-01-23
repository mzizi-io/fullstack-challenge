from src.core.db.session_factory import session_factory


async def get_db_session():
    """This method provides a session for all db queries and is
    used in dependency injection

    Yields
        : an AsyncSession instance
    """
    async with session_factory as session:
        yield session
