from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from logging import getLogger
from src.core.search import Search
from src.core.schemas import SearchParams
from src.core.deps import get_db_session


logger = getLogger(__name__)

search_router = APIRouter()


@search_router.get("/{page}/{per_page}")
async def get(
    page: int,
    per_page: int,
    session: AsyncSession = Depends(get_db_session)
):
    try:
        res = await Search().get(session=session, page=page, per_page=per_page)
        return res
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=500,
            detail="Failed to return a response.")


@search_router.post("/")
async def search(
    params: SearchParams,
    session: AsyncSession = Depends(get_db_session)
):
    try:
        res = await Search().search(session=session, params=params)
        return res
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=500,
            detail="Failed to return a response.")
