from pathlib import Path
from re import search
from .environment import Environment

def get_efi_dir(environment: Environment) -> Path:
    for i, partition in enumerate(environment.partitions):
        if not bool(search('type="EFI System"', partition)):
            continue

        for [n, path] in environment.mount_points:
            if i + 1 != n:
                continue

            result = Path(path)
            return result
