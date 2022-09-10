from pathlib import Path

CWD = Path(__file__).parent

def get_static_dir() -> Path:
    return CWD / 'static'
