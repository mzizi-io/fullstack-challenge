from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from logging import getLogger
from src.core.search import Search
from src.core.deps import get_db_session

logger = getLogger(__name__)

stats_router = APIRouter()


@stats_router.get("/count")
async def count(session: AsyncSession = Depends(get_db_session)) -> int:
    try:
        res = await Search().count(session)
        return res
    except Exception as e:
        logger.error(e)


@stats_router.get("/distinct-values/by-field/{field}")
async def get_distinct_values(
    field: str, session: AsyncSession = Depends(get_db_session)
):
    try:
        res = await Search().get_distinct_values(session=session, field=field)
        return res
    except Exception as e:
        logger.error(e)


@stats_router.get("/max/by-field/{field}")
async def get_max_value(
    field: str, session: AsyncSession = Depends(get_db_session)
):
    try:
        res = await Search().max(session=session, field=field, )
        return res
    except Exception as e:
        logger.error(e)
