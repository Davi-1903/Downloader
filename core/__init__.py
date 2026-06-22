from pathlib import Path
from pytubefix import YouTube


def get_downloads_path() -> Path | None:
    home = Path.home()
    for path in home.glob(r'*/'):
        if path.name == 'Downloads':
            return path


def download_video(url: str) -> tuple[bool, str]:
    try:
        yt = YouTube(url)
        ys = yt.streams.get_highest_resolution()
        if ys is None:
            return False, yt.title

        path = get_downloads_path()
        ys.download(str(path))
        return True, yt.title

    except Exception:
        return False, ''


def download_audio(url: str) -> tuple[bool, str]:
    try:
        yt = YouTube(url)
        ys = yt.streams.get_audio_only()
        if ys is None:
            return False, yt.title

        path = get_downloads_path()
        ys.download(str(path))
        return True, yt.title

    except Exception:
        return False, ''
