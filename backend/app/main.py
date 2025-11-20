from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# FIXED: use absolute imports (important for uvicorn)
from app.api import stt, tts, query, health
from app.core.config import settings

app = FastAPI(title="Voice AI Assistant")

# CORS for Expo
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routers
app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(stt.router, prefix="/stt", tags=["stt"])
app.include_router(tts.router, prefix="/tts", tags=["tts"])
app.include_router(query.router, prefix="/query", tags=["query"])
