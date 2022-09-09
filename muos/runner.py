from atexit import register as atexit_register
from typing import List
from .environment import Environment
from .log import Log
from .step import Step

class Runner:
    environemnt: Environment

    def __init__(self, environment: Environment, steps: List[Step]) -> None:
        self.environemnt = environment
        self.steps = steps

    def run(self) -> None:
        Log.message('[environment] {}'.format(self.environemnt))

        for step in self.steps:
            Log.message('[run] {}'.format(step.name))

            step.main(self.environemnt)
            atexit_register(step.at_exit, self.environemnt)
