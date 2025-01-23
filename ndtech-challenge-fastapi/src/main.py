from fastapi import FastAPI
from logging import getLogger
from fastapi.middleware.cors import CORSMiddleware
from src.api import api_router
from src.core.constants import API_VERSION

logger = getLogger()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=f"/api/{API_VERSION}")
