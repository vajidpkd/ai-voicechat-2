from fastapi import APIRouter
from ..core.logger import logger

router = APIRouter()

@router.get("/")
def health():
    logger.info("Health check OK")
    return {"status": "ok"}
