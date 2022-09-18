from pathlib import Path
from ...environment import Environment
from ...step import Step

class UpdateVconsoleConf(Step):
    name: str = 'Update /etc/vconsole.conf'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        vconsole_conf = Path(environment.mnt) / 'etc' / 'vconsole.conf'
        vconsole_conf.write_text('\n'.join([
            'KEYMAP={}'.format(environment.keymap),
        ]))
