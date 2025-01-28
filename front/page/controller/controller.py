import requests

url = "http://localhost:8080"


class ApiText:
    def chat_input(self, prompt: str):
        response = requests.post(f"{url}/api/v1/text/chat", json={"prompt": prompt})

        if response.status_code != 200:
            return response.text
        return response.json()

    def moderactions(self, prompt: str):
        return requests.post(f"{url}/api/v1/text/moderactions", json={"prompt": prompt})


class ApiImage:
    def create_image(self, prompt: str):
        response = requests.post(
            f"{url}/api/v1/image/generation", json={"prompt": prompt}
        )

        if response.status_code != 200:
            return response.text
        return response.json()["url"]


class ApiAudio:
    def transcribe_audio(self, audio):
        return requests.post(
            f"{url}/api/v1/audio/transcription", files={"file_upload": audio}
        )

    def translations_audio(self, audio):
        return requests.post(
            f"{url}/api/v1/audio/translations", files={"file_upload": audio}
        )

    def tts_audio(self, prompt):
        return requests.post(f"{url}/api/v1/audio/tts", json={"prompt": prompt})
