from ..environment import Environment
from ..step import Step
from .end import End

class Begin(Step):
    name: str = 'Beginning of the runner...'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        print('begin')

    def at_exit(self, environment: Environment) -> None:
        End().main(environment)
