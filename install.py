#!/usr/bin/env python3

from muos import DiskFormat, Environment, FileSystem, Runner
from muos.steps import Begin, End, FormatDisk, FormatPartitions, MountPartitions, PartitionDisk, SelectDisk, SelectPacmanMirrors, SynchronizeNtp

environment = Environment(
    disk_format=DiskFormat.GPT,
    file_systems=[
        FileSystem.FAT32,
        FileSystem.EXT4,
    ],
    mnt = '/mnt',
    mount_points=[
        (2, '/'),
        (1, '/boot'),
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
    SynchronizeNtp(),
    FormatDisk(),
    PartitionDisk(),
    FormatPartitions(),
    MountPartitions(),
    End(),
])

runner.run()
