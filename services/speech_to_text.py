import os
import tempfile
import time
import speech_recognition as sr
from io import BytesIO
from pydub import AudioSegment
from shutil import which

# --- Add ffmpeg to PATH for subprocess ---
os.environ["PATH"] += os.pathsep + r"D:\softwares\ffmpeg-8.0\bin"

# --- Verify executable paths ---
ffmpeg_path = which("ffmpeg") or r"D:\softwares\ffmpeg-8.0\bin\ffmpeg.exe"
ffprobe_path = which("ffprobe") or r"D:\softwares\ffmpeg-8.0\bin\ffprobe.exe"

AudioSegment.converter = ffmpeg_path
AudioSegment.ffmpeg = ffmpeg_path
AudioSegment.ffprobe = ffprobe_path

print(f"✅ Using ffmpeg: {ffmpeg_path}")
print(f"✅ Using ffprobe: {ffprobe_path}")

def convert(file):
    tmp_path = None
    try:
        data = file.file.read()
        audio = AudioSegment.from_file(BytesIO(data))
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp_path = tmp.name
            audio.export(tmp_path, format="wav")

        r = sr.Recognizer()
        with sr.AudioFile(tmp_path) as src:
            audio_data = r.record(src)
            text = r.recognize_google(audio_data)
        return text

    except Exception as e:
        print(f"❌ Speech-to-text error: {e}")
        return f"Error: {e}"

    finally:
        if tmp_path and os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except Exception as e:
                print(f"⚠️ Cleanup error: {e}")
