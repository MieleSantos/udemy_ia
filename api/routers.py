from fastapi import APIRouter

from udemy_ia.api.v1.text_router import router as text_router  # type: ignore
from udemy_ia.api.v1.vision_router import router as image_router  # type: ignore

router = APIRouter()
router.include_router(text_router, prefix="/api/v1", tags=["CHAT"])
router.include_router(image_router, prefix="/api/v1", tags=["Image"])
