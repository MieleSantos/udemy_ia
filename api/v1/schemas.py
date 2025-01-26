from pydantic import BaseModel, field_validator


class PromptBase(BaseModel):
    prompt: str

    @field_validator("prompt")
    def prompt_image(cls, v):
        if not v:
            raise ValueError("prompt is required")
        return v


class ImageSchemaResponse(BaseModel):
    url: str
