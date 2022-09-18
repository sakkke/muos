from ..command import Command
from ..environment import Environment
from ..get_lines_as_list import get_lines_as_list
from ..get_static_dir import get_static_dir
from ..step import Step

class SelectKeymap(Step):
    name: str = 'Selecting a keymap...'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        keymaps_txt = get_static_dir() / 'keymaps.txt'
        choices = get_lines_as_list(keymaps_txt)
        result = environment.fzf.prompt(choices, '--height=10 --layout=reverse')
        keymap = result[0]
        environment.keymap = keymap
        Command.run(['loadkeys', keymap])
