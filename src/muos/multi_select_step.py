from typing import List
from .environment import Environment
from .select_step import SelectStep

class MultiSelectStep(SelectStep):
    def main(self, environment: Environment, choices: List[str]) -> None:
        self.fzf_options += ['--multi']
        super().main(environment, choices)
