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
        """Get assets in a paginated fashion. Defined by the page
        and assets per page

        Args:
            session: AsyncSession instance
            page: page
            per_page: assets per page

        Returns:
            : List of rows from search
        """
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
        """Search assets in a paginated fashion.

        Args:
            session: AsyncSession instance
            params: search params along with page and per_page

        Returns:
            : List of rows from search
        """
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
        """Get count of rows in a table

        Args:
            session: AsyncSession instance

        Returns:
            : Count of rows
        """
        try:
            rows = await session.execute(
                select(func.count()).select_from(Assets))
            return rows.scalar()
        except Exception as e:
            logger.error(e)

    async def max(self, session: AsyncSession, field) -> float:
        """Get max value of a column

        Args:
            session: AsyncSession instance
            field: column

        Returns:
            : List of rows from search
        """
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
        """Get distinct values from a column

        Args:
            session: AsyncSession instance
            field: column

        Returns:
            : List of unique values
        """
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
    ):
        """Converts a query into paginated search

        Args:
            query: Query
            page: page
            per_page: items per page

        Returns:
            : paginated query
        """
        return (
            query
            .limit(per_page)
            .offset((page - 1) * per_page)
        )

    @staticmethod
    def _get_field_from_str(field: str):
        """Get Assets column from string

        Args:
            field: column name

        Returns:
            : field object
        """
        return getattr(Assets, field)

    def _get_indexed_field_filter(
            self, params: StrSearchCondition) -> str:
        """Get indexed field filter

        Args:
            field: column name

        Returns:
            : query object
        """
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
