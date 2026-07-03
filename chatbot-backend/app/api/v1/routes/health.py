#pyright
from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/health",
    tags=["Health"],
)

@router.get("")
async def health():
    return {
        "success":True,
        "message": "Application is healthy",
    }