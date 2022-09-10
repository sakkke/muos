from subprocess import PIPE, Popen, run
from ..environment import Environment
from ..step import Step

class PartitionDisk(Step):
    description: str = 'Partitioning a disk...'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        stdin = Popen(['printf', '%s', '\n'.join(environment.partitions)], stdout=PIPE)
        run(['sfdisk', environment.disk], stdin=stdin.stdout)
