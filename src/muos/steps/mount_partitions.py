from pathlib import Path
from ..command import Command
from ..environment import Environment
from ..get_nth_partition import get_nth_partition
from ..step import Step
from .unmount_partitions import UnmountPartitions

class MountPartitions(Step):
    name: str = 'Mounting partitions...'

    def main(self, environment: Environment) -> None:
        super().main(environment)

        for (n, path) in environment.mount_points:
            mount_point = '{}{}'.format(environment.mnt, path)
            partition = get_nth_partition(environment.disk, n)

            Path(mount_point).mkdir(exist_ok=True, parents=True)
            Command.run(['mount', '--verbose', partition, mount_point])

    def at_exit(self, environment: Environment) -> None:
        UnmountPartitions().main(environment)
