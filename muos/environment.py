from enum import Enum, auto
from strenum import LowercaseStrEnum as StrEnum, UppercaseStrEnum
from pyfzf import FzfPrompt
from typing import List, Tuple
from .fzf_manager import FzfManager

class DiskFormat(StrEnum):
    DOS = auto()
    GPT = auto()

class FileSystem(Enum):
    EXT4 = auto()
    FAT32 = auto()

class FstabTag(UppercaseStrEnum):
    LABEL = auto()
    PARTLABEL = auto()
    PARTUUID = auto()
    UUID = auto()

class Environment:
    description: str
    disk: str
    disk_format: DiskFormat
    file_systems: List[str]
    fstab_tag: FstabTag
    fzf: FzfPrompt
    locales: List[str]
    main_locale = 'C.UTF-8'
    mnt = '/mnt'
    mount_points: List[Tuple[int, str]]
    pacman_mirrors: List[str]
    pacstrap_packages: List[str]
    partitions: List[str]
    time_zone = 'UTC'

    def __init__(
        self,
        description: str,
        disk_format: DiskFormat,
        file_systems: List[FileSystem],
        fstab_tag: FstabTag,
        mnt: str,
        pacstrap_packages: List[str],
        mount_points: List[Tuple[int, str]],
        partitions: List[str],
        locales: List[str]=[],
        main_locale: str='C.UTF-8',
        pacman_mirrors: List[str]=[],
        time_zone: str='UTC',
    ) -> None:
        self.description = description
        self.disk_format = disk_format
        self.file_systems = file_systems
        self.fstab_tag = fstab_tag
        self.locales = locales
        self.main_locale = main_locale
        self.mnt = mnt
        self.mount_points = mount_points
        self.pacstrap_packages = pacstrap_packages
        self.pacman_mirrors = pacman_mirrors
        self.partitions = partitions
        self.time_zone = time_zone

        self.setup_fzf()

    def setup_fzf(self) -> None:
        fzf_manager = FzfManager()
        fzf_manager.get()
        self.fzf = fzf_manager.use()
