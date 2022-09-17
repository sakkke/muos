from ..environment import Environment
from ..get_lines_as_list import get_lines_as_list
from ..get_static_dir import get_static_dir
from ..step import Step

class SelectLocales(Step):
    description: str = 'Selecting locales...'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        locales_txt = get_static_dir() / 'locales.txt'
        choices = get_lines_as_list(locales_txt)
        result = environment.fzf.prompt(choices, '--height=10 --layout=reverse --multi')
        environment.locales = result
