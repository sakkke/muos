from atexit import register as atexit_register
from typing import List
from .environment import Environment
from .log import Log
from .step import Step

class Runner:
    environment: Environment

    def __init__(self, environment: Environment, steps: List[Step]) -> None:
        self.environment = environment
        self.steps = steps

    def run(self) -> None:
        Log.message(self.environment.description)

        for step in self.steps:
            step.main(self.environment)
            atexit_register(step.at_exit, self.environment)
