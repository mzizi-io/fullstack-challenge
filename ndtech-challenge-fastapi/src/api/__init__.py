from fastapi import APIRouter
from src.api.v1.auth import auth_router
from src.api.v1.search import search_router
from src.api.v1.stats import stats_router


api_router = APIRouter()
api_router.include_router(auth_router, prefix="/auth")
api_router.include_router(search_router, prefix="/search")
api_router.include_router(stats_router, prefix="/stats")
