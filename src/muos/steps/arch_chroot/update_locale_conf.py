from pathlib import Path
from ...environment import Environment
from ...lib import create_file
from ...step import Step

class UpdateLocaleConf(Step):
    name: str = 'Update /etc/locale.conf'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        lang = environment.main_locale.split(' ')[0]
        create_file(Path(environment.mnt) / 'etc' / 'locale.conf', [
            'LANG={}'.format(lang),
        ])
