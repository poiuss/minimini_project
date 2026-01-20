import subprocess
from pathlib import Path

def download_audio(youtube_url: str) -> str:
    audio_dir = Path("input") / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)

    outtmpl = str(audio_dir / "audio.%(ext)s")

    command = [
        "yt-dlp",
        "--no-playlist",
        "-x",
        "--audio-format", "mp3",
        "-o", outtmpl,
        youtube_url
    ]

    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if result.returncode != 0:
        raise RuntimeError(
            "yt-dlp 실행 실패입니다.\n"
            "ffmpeg 설치/경로 문제거나 URL이 잘못됐을 수 있습니다.\n"
            f"{result.stderr}"
        )

    mp3_path = audio_dir / "audio.mp3"
    if not mp3_path.exists():
        raise FileNotFoundError(f"mp3 파일이 생성되지 않았습니다: {mp3_path}")

    return str(mp3_path)