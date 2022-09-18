from pathlib import Path
from typing import List
from .command import Command

class Pacman:
    options: List[str]

    def __init__(self, options: List[str]=['--color', 'auto', '--noprogressbar']) -> None:
        self.options = options

    def add(self, mnt: Path, packages: List[str]):
        Command.run(['arch-chroot', mnt, 'pacman', '--noconfirm', '--sync'] + self.options + packages)

    def bootstrap(self, mnt: Path, packages: List[str], options: List[str]=[]):
        Command.run(['pacstrap'] + options + [mnt] + self.options + packages)
