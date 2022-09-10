from ..command import Command
from ..environment import Environment
from ..step import Step

class UnmountPartitions(Step):
    name: str = 'Unmount partitions'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        Command.run(['umount', '--recursive', '--verbose', environment.mnt])
