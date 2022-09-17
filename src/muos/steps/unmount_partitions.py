from ..command import Command
from ..environment import Environment
from ..step import Step

class UnmountPartitions(Step):
    description: str = 'Unmounting partitions...'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        Command.run(['umount', '--recursive', '--verbose', environment.mnt])
