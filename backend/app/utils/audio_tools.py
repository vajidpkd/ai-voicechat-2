from pydub import AudioSegment
from pathlib import Path

def convert_to_wav(src: str, dst: str):
    src_p = Path(src)
    dst_p = Path(dst)
    audio = AudioSegment.from_file(str(src_p))
    audio = audio.set_frame_rate(16000).set_channels(1)
    audio.export(str(dst_p), format="wav")
    return str(dst_p)
