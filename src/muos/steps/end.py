from ..environment import Environment
from ..step import Step

class End(Step):
    description: str = 'Ending of the runner...'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        print('end')
