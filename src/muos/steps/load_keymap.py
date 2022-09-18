from ..command import Command
from ..environment import Environment
from ..step import Step

class LoadKeymap(Step):
    name: str = 'Load keymap'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        Command.run(['loadkeys', environment.keymap])
