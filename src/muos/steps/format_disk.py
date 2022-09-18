from subprocess import PIPE, Popen, run
from ..environment import Environment
from ..step import Step

class FormatDisk(Step):
    name: str = 'Formatting a disk...'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        stdin = Popen(['printf', '%s', 'label: {}'.format(environment.disk_format)], stdout=PIPE)
        run(['sfdisk', environment.disk], stdin=stdin.stdout)
