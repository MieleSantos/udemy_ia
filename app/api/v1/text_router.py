from fastapi import APIRouter, HTTPException

from app.api.v1.schemas import PromptBase
from app.services.openai_service import AssistentIA

router = APIRouter()

assistent = AssistentIA()


@router.post("/text/chat", description="This endpoint is used to chat with the AI")
async def chat_input(prompt: PromptBase):
    try:
        response = assistent.chat_input(prompt.prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return response


@router.post(
    "/text/moderactions", description="This endpoint is used to moderate the chat"
)
async def moderactions_input(prompt: PromptBase):
    try:
        response = assistent.chat_moderation(prompt.prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return response
