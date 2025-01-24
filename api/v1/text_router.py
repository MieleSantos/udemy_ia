from fastapi import APIRouter

from udemy_ia.services.open_ai import AssistentIA

router = APIRouter()


@router.post("/text/chat")
async def chat_input(message: str):
    chat = AssistentIA()
    return chat.chat_input(message)
