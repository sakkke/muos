from ..environment import Environment
from ..get_lines_as_list import get_lines_as_list
from ..get_static_dir import get_static_dir
from ..multi_select_step import MultiSelectStep

class SelectLocales(MultiSelectStep):
    name: str = 'Select locales'

    def main(self, environment: Environment) -> None:
        super().main(environment, get_lines_as_list(get_static_dir() / 'locales.txt'))
        environment.locales = self.choices
