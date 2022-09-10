from ..environment import Environment
from ..step import Step

class Begin(Step):
    name: str = 'Begin'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        print('begin')
