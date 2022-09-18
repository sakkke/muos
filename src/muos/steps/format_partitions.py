from ..command import Command
from ..environment import Environment, FileSystem
from ..get_nth_partition import get_nth_partition
from ..step import Step

class FormatPartitions(Step):
    name: str = 'Formatting partitions...'

    def main(self, environment: Environment) -> None:
        super().main(environment)

        for i, file_system in enumerate(environment.file_systems):
            partition = get_nth_partition(environment.disk, i + 1)

            if file_system == FileSystem.EXT4:
                Command.run(['mkfs.ext4', '-F', partition])
                continue

            if file_system == FileSystem.FAT32:
                Command.run(['mkfs.fat', '-F', '32', partition])
                continue
