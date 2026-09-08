import os

from dotenv import load_dotenv
from fastapi import UploadFile, File
from google import genai
from google.genai import types
from gemini_tools import GeminiTools

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")


class GeminiService:
    def __init__(self):
        self.client = genai.Client(api_key=gemini_api_key)

    def chat_with_gemini(self, message: str, file: UploadFile):
        # Читаем байты из объекта UploadFile
        file_bytes = file.file.read()

        # Формируем объект Part для Gemini
        document_part = types.Part.from_bytes(
            data=file_bytes,
            mime_type=file.content_type or "application/pdf"
        )
        response = self.client.models.generate_content(
            model="gemini-3.5-flash",
            contents=[message, document_part],
            config=types.GenerateContentConfig(
                tools=[
                    GeminiTools.gemini_request_to_create_new_user,
                ]
            )
        )
        return response.text