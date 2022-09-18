from typing import List
from .environment import Environment
from .step import Step

class SelectStep(Step):
    choices: List
    fzf_options: List[str] = ['--height=10', '--layout=reverse']

    def main(self, environment: Environment, choices: List[str]) -> None:
        super().main(environment)
        self.choices = environment.fzf.prompt(choices, ' '.join(self.fzf_options))
