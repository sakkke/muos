#!/usr/bin/env python3

from muos import (
    DiskFormat,
    Environment,
    FileSystem,
    FstabTag,
    Runner,
)

from muos.steps import (
    Begin,
    BootstrapArchLinux,
    FormatDisk,
    FormatPartitions,
    GenerateFstab,
    MountPartitions,
    PartitionDisk,
    SelectDisk,
    SelectPacmanMirrors,
    SelectTimeZone,
    SynchronizeNtp,
)

environment = Environment(
    description='Installing muOS...',
    disk_format=DiskFormat.GPT,
    file_systems=[
        FileSystem.FAT32,
        FileSystem.EXT4,
    ],
    fstab_tag=FstabTag.UUID,
    mnt = '/mnt',
    mount_points=[
        (2, '/'),
        (1, '/boot'),
    ],
    pacstrap_packages=[
        'base',
        'linux',
        'linux-firmware',
    ],
    partitions=[
        'size=300MiB, type="EFI System"',
        'type="Linux root (x86-64)"',
    ],
)

runner = Runner(environment, [
    Begin(),
    SelectDisk(),
    SelectPacmanMirrors(),
    SelectTimeZone(),
    SynchronizeNtp(),
    FormatDisk(),
    PartitionDisk(),
    FormatPartitions(),
    MountPartitions(),
    BootstrapArchLinux(),
    GenerateFstab(),
])

runner.run()
