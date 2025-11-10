from fastapi import FastAPI, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from services import speech_to_text, text_translator, text_to_speech
import os

app = FastAPI()

# Directory to store generated audio files
AUDIO_DIR = "audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

# Mount directory to serve audio files via URL
app.mount("/audio", StaticFiles(directory=AUDIO_DIR), name="audio")


@app.get("/")
def root():
    return {"message": "Translator backend running"}


@app.post("/translate-text")
def translate_text(request: dict):
    """
    Translate plain text to target language and generate TTS audio.
    Returns translation and audio URL.
    """
    text = request.get("text")
    target_lang = request.get("target_lang")

    if not text:
        return JSONResponse({"error": "No text provided"}, status_code=400)

    # Translate text
    translated_text = text_translator.translate(text, target_lang)

    # Generate TTS audio
    audio_file_path = text_to_speech.convert(translated_text, lang=target_lang)
    audio_url = f"http://127.0.0.1:8000/audio/{os.path.basename(audio_file_path)}"

    return JSONResponse({"translated_text": translated_text, "audio": audio_url})


@app.post("/translate-voice")
async def translate_voice(file: UploadFile, target_lang: str = Form(...)):
    """
    Convert uploaded voice file to text, translate it, and generate TTS audio.
    Returns translation and audio URL.
    """
    if not file:
        return JSONResponse({"error": "No file uploaded"}, status_code=400)

    # Convert voice to text
    input_text = speech_to_text.convert(file)
    if not input_text:
        return JSONResponse({"error": "Could not recognize speech"}, status_code=400)

    # Translate text
    translated_text = text_translator.translate(input_text, target_lang)

    # Generate TTS audio
    audio_file_path = text_to_speech.convert(translated_text, lang=target_lang)
    audio_url = f"http://127.0.0.1:8000/audio/{os.path.basename(audio_file_path)}"

    return JSONResponse({"translated_text": translated_text, "audio": audio_url})
