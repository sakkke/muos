#!/usr/bin/env python3

from muos import Runner
from muos.steps import Begin, SynchronizeNtp

runner = Runner([
    Begin(),
    SynchronizeNtp(),
])

runner.run()
