import time

from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
class GeminiService:
    def __init__(self):
        self.client = genai.Client(api_key=gemini_api_key)

    def chat_with_gemini(self,message: str):
        start = time.perf_counter()
        # generate_config = types.ChatGenerateConfig(
        #     types.
        # )
        interaction = self.client.interactions.create(
            model="gemini-3.5-flash",
            input=message,
        )
        print(f"2. Google ответил за {time.perf_counter() - start:.2f} сек")
        return interaction.output_text

gemini_service = GeminiService()
gemini_service.chat_with_gemini("hello")