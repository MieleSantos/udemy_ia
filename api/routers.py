from fastapi import APIRouter

from udemy_ia.api.v1.text_router import router as text_router

router = APIRouter()
router.include_router(text_router, prefix="/api/v1", tags=["CHAT"])
