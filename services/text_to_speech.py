from gtts import gTTS
import os

def convert(text, lang="en"):
    os.makedirs("audio", exist_ok=True)
    file_name = f"audio/tts_{abs(hash(text))}.mp3"
    tts = gTTS(text=text, lang=lang)
    tts.save(file_name)
    return file_name