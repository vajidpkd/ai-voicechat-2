from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
import uuid
from ..core.config import settings
from ..services.tts_service import text_to_speech_gtts
from ..core.logger import logger

router = APIRouter()
TTS_DIR = Path(settings.TTS_DIR)
TTS_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/speak")
def speak(text: str = Form(...)):
    try:
        fname = f"{uuid.uuid4().hex}.mp3"
        out_path = TTS_DIR / fname
        text_to_speech_gtts(text, out_path=str(out_path))
        logger.info(f"Generated tts: {out_path}")
        # Return path to client (FileResponse also possible)
        return {"audio_url": f"/tts/file/{fname}"}
    except Exception as e:
        logger.exception("TTS failure")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/file/{filename}")
def get_file(filename: str):
    path = TTS_DIR / filename
    if not path.exists():
        raise HTTPException(status_code=404, detail="Not found")
    return FileResponse(str(path), media_type="audio/mpeg", filename=filename)
