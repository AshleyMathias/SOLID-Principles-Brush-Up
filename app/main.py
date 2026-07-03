from fastapi import FastAPI

from app.routers.health import router as health_router


app=FastAPI(
    title="Production Chabot API",
    description="Production-grade chabot backend built with FastAPI",
    version="1.0.0"
)

app.include_router(health_router)


@app.get("/")
async def root():
    return{
        "message":"Production chatbot API is running"
    }