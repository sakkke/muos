#!/usr/bin/env python3

from muos import Environment, Runner
from muos.steps import Begin, End, SelectDisk, SynchronizeNtp

environment = Environment()

runner = Runner(environment, [
    Begin(),
    SelectDisk(),
    SynchronizeNtp(),
    End(),
])

runner.run()
