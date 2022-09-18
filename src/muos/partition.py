from pathlib import Path
from .environment import FileSystem
from .partition_type import PartitionType

class Partition:
    filesystem: FileSystem
    '''Filesystem of partition

    Example: ``FileSystem.FAT32``
    '''

    mountpoint: Path
    '''Mountpoint of partition

    Example: ``/boot``
    '''

    size: str
    '''Size of partition

    Example: ``300MiB``
    '''

    type: PartitionType
    '''Type of partition

    Example:
        ``PartitionType.EFI_SYSTEM``

        ``'efi_system'``
        Same as above.
    '''
