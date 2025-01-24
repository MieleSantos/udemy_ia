import os

from dotenv import load_dotenv
from openai import OpenAI


class AssistentIA:
    def __init__(self):
        self._set_env()
        self.client = OpenAI()

    def _set_env(self):
        load_dotenv()
        if not os.getenv("OPEN_API_KEY"):
            raise ValueError("OPEN_API_KEY not found")

        os.environ["OPENAI_API_KEY"] = os.getenv("OPEN_API_KEY")

    def chat_input(self, message: str):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}],
        )

        return completion.choices[0].message

    # return completion.choices[0].message.content
