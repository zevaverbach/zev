from pathlib import Path


def get_filesize(path: str) -> int:
    return Path(path).stat().st_size
