#!/usr/bin/env python3

from muos import DiskFormat, Environment, FileSystem, Runner
from muos.steps import Begin, End, FormatDisk, FormatPartitions, PartitionDisk, SelectDisk, SynchronizeNtp

environment = Environment(
    disk_format=DiskFormat.GPT,
    file_systems=[
        FileSystem.FAT32,
        FileSystem.EXT4,
    ],
    partitions=[
        'size=300MiB, type="EFI System"',
        'type="Linux root (x86-64)"',
    ],
)

runner = Runner(environment, [
    Begin(),
    SelectDisk(),
    SynchronizeNtp(),
    FormatDisk(),
    PartitionDisk(),
    FormatPartitions(),
    End(),
])

runner.run()
