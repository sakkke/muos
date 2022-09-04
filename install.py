#!/usr/bin/env python3

from muos import Environment, Runner
from muos.steps import Begin, End, SynchronizeNtp

environment = Environment()

runner = Runner(environment, [
    Begin(),
    SynchronizeNtp(),
    End(),
])

runner.run()
