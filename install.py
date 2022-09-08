#!/usr/bin/env python3

from muos import DiskFormat, Environment, Runner
from muos.steps import Begin, End, FormatDisk, SelectDisk, SynchronizeNtp

environment = Environment(
    disk_format=DiskFormat.GPT,
)

runner = Runner(environment, [
    Begin(),
    SelectDisk(),
    SynchronizeNtp(),
    FormatDisk(),
    End(),
])

runner.run()
