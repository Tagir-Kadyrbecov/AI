from fastapi import FastAPI
from routers.gemini_route import router as gemini_router
app = FastAPI()
app.include_router(gemini_router)
