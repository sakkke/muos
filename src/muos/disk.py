from pathlib import Path
from typing import List
from .environment import DiskFormat
from .partition import Partition

class Disk:
    format: DiskFormat
    '''A format of disk

    Example: ``DiskFormat.GPT``
    '''

    mountpoint: Path
    '''Mountpoint of disk

    Example: ``Path('/mnt')``
    '''

    partitions: List[Partition]
    '''Array for partitions

    Example: ``[Partition()]``
    '''

    path: Path
    '''Path of disk

    Example: ``Path('/dev/sda')``
    '''
