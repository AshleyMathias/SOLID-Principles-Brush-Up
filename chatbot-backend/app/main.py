# pyright: reportMissingImports=false
from fastapi import FastAPI

from app.api.v1.routes.health import router as health_router

app = FastAPI(
    title="Production Chabot Backend",
    version="1.0.0",
)

app.include_router(health_router)

