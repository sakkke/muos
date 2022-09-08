#!/usr/bin/env python3

from muos import DiskFormat, Environment, Runner
from muos.steps import Begin, End, FormatDisk, PartitionDisk, SelectDisk, SynchronizeNtp

environment = Environment(
    disk_format=DiskFormat.GPT,
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
    End(),
])

runner.run()
