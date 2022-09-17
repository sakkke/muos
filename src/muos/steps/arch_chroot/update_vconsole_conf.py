from pathlib import Path
from ...environment import Environment
from ...step import Step

class UpdateVconsoleConf(Step):
    description: str = 'Updating /etc/vconsole.conf...'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        vconsole_conf = Path(environment.mnt) / 'etc' / 'vconsole.conf'
        lang = environment.main_locale.split(' ')[0]
        vconsole_conf.write_text('\n'.join([
            'KEYMAP={}'.format(environment.keymap),
            'LANG={}'.format(lang),
        ]))
