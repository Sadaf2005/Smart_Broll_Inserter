import whisper
from pathlib import Path
import subprocess

model = whisper.load_model("base")


def extract_audio(video_path: str, audio_path: str):
    audio_path = Path(audio_path)
    audio_path.parent.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i", video_path,
            "-vn",
            "-acodec", "mp3",
            str(audio_path)
        ],
        check=True
    )


def transcribe_audio(audio_path: str):
    result = model.transcribe(audio_path)

    segments = []
    for seg in result["segments"]:
        segments.append({
            "start": seg["start"],
            "end": seg["end"],
            "text": seg["text"]
        })

    return segments
