from fastapi import APIRouter
from api import ai_route

api_router = APIRouter()

api_router.include_router(
    ai_route.router,
    prefix='/vectorize',
    tags=['Face features extraction to vector']
)
