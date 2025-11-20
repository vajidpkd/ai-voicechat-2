from fastapi import APIRouter, Form, HTTPException
from ..services.wiki_service import search_wiki_summary
from ..services.tts_service import text_to_speech_gtts
from ..core.logger import logger
from pathlib import Path
import uuid
from ..core.config import settings

router = APIRouter()

@router.post("/wiki")
def wiki_text(text: str = Form(...), voice: bool = Form(False)):
    try:
        summary = search_wiki_summary(text, sentences=3)
        if voice:
            fname = f"{uuid.uuid4().hex}.mp3"
            out_path = Path(settings.TTS_DIR) / fname
            out_path.parent.mkdir(parents=True, exist_ok=True)
            text_to_speech_gtts(summary, out_path=str(out_path))
            return {"text": summary, "audio_url": f"/tts/file/{fname}"}
        return {"text": summary}
    except Exception as e:
        logger.exception("Wiki failure")
        raise HTTPException(status_code=500, detail=str(e))
