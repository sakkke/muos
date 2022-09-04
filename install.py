#!/usr/bin/env python3

from muos import Runner
from muos.steps import Begin, End, SynchronizeNtp

runner = Runner([
    Begin(),
    SynchronizeNtp(),
    End(),
])

runner.run()
