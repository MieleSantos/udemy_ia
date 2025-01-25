from fastapi import APIRouter, HTTPException

from udemy_ia.services.open_ai import AssistentIA

router = APIRouter()

assistent = AssistentIA()


@router.post("/text/chat", description="This endpoint is used to chat with the AI")
async def chat_input(message: str):
    try:
        response = assistent.chat_input(message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return response


@router.post(
    "/text/moderactions", description="This endpoint is used to moderate the chat"
)
async def moderactions_input(message: str):
    try:
        response = assistent.chat_moderation(message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return response
