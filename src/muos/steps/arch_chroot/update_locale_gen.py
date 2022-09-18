from pathlib import Path
from ...environment import Environment
from ...step import Step

class UpdateLocaleGen(Step):
    name: str = 'Update /etc/locale.gen'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        locale_gen = Path(environment.mnt) / 'etc' / 'locale.gen'
        content = locale_gen.read_text()
        locale = environment.locales

        for locale in environment.locales:
            content = content.replace('#{}'.format(locale), locale)

        locale_gen.write_text(content)
