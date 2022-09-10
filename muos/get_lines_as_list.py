from os import PathLike
from pathlib import Path
from typing import List

def get_lines_as_list(path: PathLike) -> List[str]:
    return Path(path).read_text().split('/n')
