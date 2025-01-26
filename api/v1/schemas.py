from pydantic import BaseModel, field_validator


class PromptBase(BaseModel):
    prompt_image: str

    @field_validator("prompt_image")
    def prompt_image(cls, v):
        if not v:
            raise ValueError("prompt_image is required")
        return v


class ImageSchemaResponse(BaseModel):
    url: str
