from ...command import Command
from ...environment import Environment
from ...step import Step

class GenerateAdjtime(Step):
    description: str = 'Generating /etc/adjtime...'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        Command.run(['arch-chroot', environment.mnt, 'hwclock', '--systohc'])
