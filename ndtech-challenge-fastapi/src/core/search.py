from sqlalchemy import func, select, and_
from logging import getLogger
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.models import Assets
from src.core.db.session_factory import session_factory
from src.core.schemas import (
    SearchParams,
    StrSearchCondition,
    SearchTypes,
    RangeSearchCondition
)
from src.core.schemas import AssetSearchResponse, AssetSearchRow

logger = getLogger(__name__)


class Search:
    def __init__(self) -> None:
        self.session_factory = session_factory

    async def get(
        self, session: AsyncSession, page: int, per_page: int
    ) -> AssetSearchResponse:
        try:
            query = self._paginated_search_query(
                select(Assets), page, per_page)
            res = await session.execute(query)
            res = res.scalars().all()
            return AssetSearchResponse(
                assets=[
                    AssetSearchRow.model_validate(asset) for asset in res
                ]
            )
        except Exception as e:
            logger.error(e)

    async def search(
        self,
        session: AsyncSession,
        params: SearchParams
    ) -> AssetSearchResponse:
        filters = self._get_filters(params.params)
        try:
            query = self._paginated_search_query(
                select(Assets).where(and_(*filters)),
                page=params.page,
                per_page=params.per_page,
            )
            res = await session.execute(query)
            res = res.scalars().all()
            return AssetSearchResponse(
                assets=[
                    AssetSearchRow.model_validate(asset) for asset in res
                ]
            )

        except Exception as e:
            logger.error(e)

    async def count(self, session: AsyncSession) -> int:
        try:
            rows = await session.execute(
                select(func.count()).select_from(Assets))
            return rows.scalar()
        except Exception as e:
            logger.error(e)

    async def max(self, session: AsyncSession, field) -> float:
        try:
            field = self._get_field_from_str(field)
            rows = await session.execute(
                select(func.max(field))
            )
            return rows.scalar()
        except Exception as e:
            logger.error(e)

    async def get_distinct_values(
        self, session: AsyncSession, field: str
    ) -> List:
        try:
            field = self._get_field_from_str(field)
            rows = await session.execute(
                select(field.distinct())
            )
            return rows.scalars().all()
        except Exception as e:
            logger.error(e)

    def _paginated_search_query(
        self,
        query,
        page: int,
        per_page: int
    ) -> AssetSearchResponse:
        """Converts a query into paginated search
        """
        return (
            query
            .limit(per_page)
            .offset((page - 1) * per_page)
        )

    @staticmethod
    def _get_field_from_str(field):
        return getattr(Assets, field)

    def _get_indexed_field_filter(
            self, params: StrSearchCondition) -> str:
        filter = func\
            .to_tsvector("english", self._get_field_from_str(params.field))\
            .op("@@")(
                func.plainto_tsquery("english", params.value))
        return filter

    def _get_numeric_field_filter(
            self, params: RangeSearchCondition) -> AssetSearchResponse:
        return and_(
            self._get_field_from_str(params.field) >= params.min,
            self._get_field_from_str(params.field) <= params.max
        )

    def _get_exact_string_field_filter(
            self, params: RangeSearchCondition) -> AssetSearchResponse:
        return self._get_field_from_str(params.field) == params.value

    def _get_filters(
            self, params: SearchParams
    ) -> List:
        filters = []
        for param in params:
            if param.search_type == SearchTypes.RANGE:
                filters.append(
                    self._get_numeric_field_filter(param)
                )
            elif param.search_type == SearchTypes.EXACT_STRING:
                filters.append(
                    self._get_exact_string_field_filter(param)
                )
            else:
                filters.append(
                    self._get_indexed_field_filter(param)
                )
        return filters
