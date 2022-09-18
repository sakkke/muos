from pathlib import Path
from ..command import Command
from ..environment import Environment
from ..step import Step

class GenerateFstab(Step):
    name: str = 'Generating /etc/fstab...'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        genfstab = Command.capture(['genfstab', '-t', environment.fstab_tag, environment.mnt])
        fstab = Path(environment.mnt) / 'etc' / 'fstab'

        with fstab.open('a') as f:
            f.write('\n{}'.format(genfstab.stdout))
