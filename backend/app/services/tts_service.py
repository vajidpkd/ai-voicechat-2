from gtts import gTTS
from pathlib import Path

def text_to_speech_gtts(text: str, out_path: str, lang="en"):
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    tts = gTTS(text=text, lang=lang)
    tts.save(str(out_path))
    return str(out_path)
