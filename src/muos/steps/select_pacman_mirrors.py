from ..environment import Environment
from ..get_lines_as_list import get_lines_as_list
from ..get_static_dir import get_static_dir
from ..multi_select_step import MultiSelectStep

class SelectPacmanMirrors(MultiSelectStep):
    name: str = 'Select Pacman mirrors'

    def main(self, environment: Environment) -> None:
        super().main(environment, get_lines_as_list(get_static_dir() / 'pacman_mirrors.txt'))
        environment.pacman_mirrors = self.choices
