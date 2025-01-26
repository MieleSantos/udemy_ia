from enum import Enum


class ServicesOptions(str, Enum):
    groq = "groq"
    openai = "openai"


# def select_model():  # noqa: PLR6301
#     model_options = [
#         "gpt-3.5-turbo",
#         "gpt-4",
#         "gpt-4-turbo",
#         "gpt-4o-mini",
#         "gpt-4o",
#         "groq",
#     ]

#     return model_options
