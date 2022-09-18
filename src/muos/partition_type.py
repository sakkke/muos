from enum import auto
from strenum import LowercaseStrEnum as StrEnum

class PartitionType(StrEnum):
    EFI_SYSTEM = auto()
    LINUX_ROOT_X86_64 = auto()
