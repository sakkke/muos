from pathlib import Path
from ...environment import Environment
from ...step import Step

class UpdateLocaleConf(Step):
    name: str = 'Update /etc/locale.conf'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        locale_conf = Path(environment.mnt) / 'etc' / 'locale.conf'
        lang = environment.main_locale.split(' ')[0]
        locale_conf.write_text('\n'.join([
            'LANG={}'.format(lang),
        ]))
