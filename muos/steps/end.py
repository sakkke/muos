from ..environment import Environment
from ..step import Step

class End(Step):
    name: str = 'End'

    def main(self, environment: Environment) -> None:
        print('end')
