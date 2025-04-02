from fastapi import APIRouter
from app.api.v1.endpoints import auth
from app.core.config import settings

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"]) 