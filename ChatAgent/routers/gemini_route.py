from fastapi import APIRouter
from gemini_client.gemini_service import GeminiService
router = APIRouter()
gemini_service = GeminiService()

@router.post("/chat", tags=["chat"])
def chat(message: str):
    return gemini_service.chat_with_gemini(message)