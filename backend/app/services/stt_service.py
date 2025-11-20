import speech_recognition as sr

def audiofile_to_text_google(filepath: str) -> str:
    r = sr.Recognizer()
    with sr.AudioFile(filepath) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        raise RuntimeError(f"STT request error: {e}")
