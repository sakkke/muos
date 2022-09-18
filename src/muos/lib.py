from pathlib import Path
from typing import List

def create_file(path: Path, lines: List[str]):
    path.write_text('\n'.join(lines))
