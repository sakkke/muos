#!/usr/bin/env python3

from muos import Runner
from muos.steps import Begin

runner = Runner([
    Begin(),
])

runner.run()
