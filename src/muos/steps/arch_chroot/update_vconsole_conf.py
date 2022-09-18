from pathlib import Path
from ...environment import Environment
from ...lib import create_file
from ...step import Step

class UpdateVconsoleConf(Step):
    name: str = 'Update /etc/vconsole.conf'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        create_file(Path(environment.mnt) / 'etc' / 'vconsole.conf', [
            'KEYMAP={}'.format(environment.keymap),
        ])
