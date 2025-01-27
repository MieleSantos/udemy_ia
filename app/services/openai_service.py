import os

from dotenv import load_dotenv
from openai import OpenAI
import io


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
            # messages=[{"role": "user", "content": message}],
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ],
        )

        return completion.choices[0].message

    def chat_moderation(self, message: str):
        response = self.client.moderations.create(
            model="omni-moderation-latest", input=message
        )
        return response

    def image_generation(self, prompt_image: str):
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=prompt_image,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        return response

    def audio_generation(self, prompt_audio: str):
        response = self.client.audio.speech.create(
            model="tts-1",
            input=prompt_audio,
            voice="echo",
        )
        return io.BytesIO(response.content)

    def audio_transcription(self, prompt_audio: io.BytesIO):
        transcription = self.client.audio.transcriptions.create(
            model="whisper-1",
            file=prompt_audio,
            language="en",
        )
        return transcription.text
