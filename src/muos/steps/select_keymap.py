from ..command import Command
from ..environment import Environment
from ..get_lines_as_list import get_lines_as_list
from ..get_static_dir import get_static_dir
from ..select_step import SelectStep

class SelectKeymap(SelectStep):
    name: str = 'Select a keymap'

    def main(self, environment: Environment) -> None:
        super().main(environment, get_lines_as_list(get_static_dir() / 'keymaps.txt'))
        environment.keymap = self.choices[0]
        Command.run(['loadkeys', environment.keymap])
