from enum import Enum, auto
from strenum import LowercaseStrEnum as StrEnum
from pyfzf import FzfPrompt
from typing import List, Tuple
from .fzf_manager import FzfManager

class DiskFormat(StrEnum):
    DOS = auto()
    GPT = auto()

class FileSystem(Enum):
    EXT4 = auto()
    FAT32 = auto()

class Environment:
    description: str
    disk: str
    disk_format: DiskFormat
    file_systems: List[str]
    fzf: FzfPrompt
    mnt = '/mnt'
    mount_points: List[Tuple[int, str]]
    pacman_mirrors: List[str]
    partitions: List[str]

    def __init__(
        self,
        description: str,
        disk_format: DiskFormat,
        file_systems: List[FileSystem],
        mnt: str,
        mount_points: List[Tuple[int, str]],
        partitions: List[str],
        pacman_mirrors: List[str]=[],
    ) -> None:
        self.description = description
        self.disk_format = disk_format
        self.file_systems = file_systems
        self.mnt = mnt
        self.mount_points = mount_points
        self.pacman_mirrors = pacman_mirrors
        self.partitions = partitions

        self.setup_fzf()

    def setup_fzf(self) -> None:
        fzf_manager = FzfManager()
        fzf_manager.get()
        self.fzf = fzf_manager.use()
