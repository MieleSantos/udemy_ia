from fastapi import APIRouter, HTTPException

from udemy_ia.services.openai_service import AssistentIA
from udemy_ia.api.v1.schemas import PromptBase, ImageSchemaResponse

router = APIRouter()

assistent = AssistentIA()


@router.post(
    "/image/generation",
    description="This endpoint is used to generate images",
    response_model=ImageSchemaResponse,
)
async def image_generation(prompt_image: PromptBase) -> ImageSchemaResponse:
    try:
        response = assistent.image_generation(prompt_image.prompt_image)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return response.data[0].url
