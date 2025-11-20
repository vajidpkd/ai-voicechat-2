from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
import shutil, uuid
from ..core.config import settings
from ..services.stt_service import audiofile_to_text_google
from ..core.logger import logger

router = APIRouter()

UPLOAD_DIR = Path(settings.UPLOAD_DIR)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/")
async def transcribe(file: UploadFile = File(...)):
    try:
        uid = uuid.uuid4().hex
        ext = Path(file.filename).suffix or ".wav"
        dest = UPLOAD_DIR / f"{uid}{ext}"
        with dest.open("wb") as out:
            shutil.copyfileobj(file.file, out)
        logger.info(f"Saved upload: {dest}")
        text = audiofile_to_text_google(str(dest))
        return {"text": text}
    except Exception as e:
        logger.exception("STT failure")
        raise HTTPException(status_code=500, detail=str(e))
