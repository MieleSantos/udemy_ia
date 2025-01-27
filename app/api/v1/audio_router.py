from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.api.v1.schemas import PromptBase


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
