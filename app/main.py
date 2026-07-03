from fastapi import FastAPI

from app.core.config import settings
from app.routers.health import router as health_router


app=FastAPI(
    title=settings.PROJECT_NAME,
    description="Production-grade chabot backend built with FastAPI",
    version=settings.API_VERSION
)

app.include_router(health_router)


@app.get("/")
async def root():
    return{
        "application":settings.PROJECT_NAME,
        "environment":settings.ENVIRONMENT,
        "version": settings.API_VERSION,
        "status": "running"
    }