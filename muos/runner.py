from typing import List
from .step import Step

class Runner:
    def __init__(self, steps: List[Step]) -> None:
        self.steps = steps

    def run(self) -> None:
        for step in self.steps:
            print('run: {}'.format(step.name))

            step.main()
