from fastapi import APIRouter

auth_router = APIRouter()


@auth_router.get("")
async def login():
    return "Logged in"
