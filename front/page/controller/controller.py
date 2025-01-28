import requests

url = "http://localhost:8080"


class Api:
    def chat_input(self, prompt: str):
        response = requests.post(f"{url}/api/v1/text/chat", json={"prompt": prompt})

        if response.status_code != 200:
            return response.text
        return response.json()

    def create_image(self, prompt: str):
        response = requests.post(
            f"{url}/api/v1/image/generation", json={"prompt": prompt}
        )

        if response.status_code != 200:
            return response.text
        return response.json()["url"]

    def transcribe_audio(self, audio):
        return requests.post(
            f"{url}/api/v1/audio/transcription", files={"file_upload": audio}
        )
