from fastapi import APIRouter, UploadFile, File
from gemini_client.gemini_service import GeminiService
router = APIRouter()
gemini_service = GeminiService()

@router.post("/chat", tags=["chat"])
def chat(message: str, file: UploadFile | None = File(default=None)):
    if file is not None:
        print("Пользователь прикрепил файл")
    return gemini_service.chat_with_gemini(message, file)

# @router.post("/upload")
# async def upload_pdf(file: UploadFile = File(...)):
#     return await gemini_service.parse_pdf(file)