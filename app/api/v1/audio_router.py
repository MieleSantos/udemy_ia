from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import StreamingResponse
from app.api.v1.schemas import PromptBase
import io

from app.services.openai_service import AssistentIA

router = APIRouter()

assistent = AssistentIA()


@router.post("/audio/tts", description="This endpoint is used to chat with the AI")
async def audio_input(prompt: PromptBase):
    try:
        audio_bytes = assistent.audio_generation(prompt.prompt)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return StreamingResponse(content=audio_bytes, media_type="audio/mp3")


@router.post(
    "/audio/transcription", description="This endpoint is used to chat with the AI"
)
async def transcription_input(file_upload: UploadFile = File(...)):
    try:
        audio_read = await file_upload.read()
        audio_bytes = io.BytesIO(audio_read)
        audio_bytes.name = "transcription.mp3"
        audio_text = assistent.audio_transcription(audio_bytes)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return audio_text
