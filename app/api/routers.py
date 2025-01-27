from fastapi import APIRouter

from app.api.v1.text_router import router as text_router
from app.api.v1.vision_router import router as image_router
from app.api.v1.audio_router import router as audio_router

router = APIRouter()
router.include_router(text_router, prefix="/api/v1", tags=["CHAT_TEXT"])
router.include_router(image_router, prefix="/api/v1", tags=["CHAT_IMAGE"])
router.include_router(audio_router, prefix="/api/v1", tags=["CHAT_AUDIO"])