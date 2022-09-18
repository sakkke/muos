from ...command import Command
from ...environment import Environment
from ...step import Step

class GenerateLocales(Step):
    name: str = 'Generating locales...'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        Command.run(['arch-chroot', environment.mnt, 'locale-gen'])
