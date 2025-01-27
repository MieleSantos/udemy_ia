from fastapi import APIRouter, HTTPException

from app.api.v1.schemas import ImageSchemaResponse, PromptBase
from app.services.openai_service import AssistentIA

router = APIRouter()

assistent = AssistentIA()


@router.post(
    "/image/generation",
    description="This endpoint is used to generate images",
    response_model=ImageSchemaResponse,
)
async def image_generation(prompt_image: PromptBase) -> ImageSchemaResponse:
    try:
        response = assistent.image_generation(prompt_image.prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"url": response.data[0].url}
