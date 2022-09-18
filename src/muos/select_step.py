from typing import List
from .environment import Environment
from .step import Step

class SelectStep(Step):
    choices: List

    def main(self, environment: Environment, choices: List[str]) -> None:
        super().main(environment)
        self.choices = environment.fzf.prompt(choices, '--height=10 --layout=reverse --multi')
