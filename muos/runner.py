from typing import List
from .color import Color
from .step import Step

class Runner:
    def __init__(self, steps: List[Step]) -> None:
        self.steps = steps

    def run(self) -> None:
        for step in self.steps:
            print('{}[run] {}{}'.format(Color.GREEN, step.name, Color.DEFAULT))

            step.main()
