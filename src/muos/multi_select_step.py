from typing import List
from .environment import Environment
from .select_step import SelectStep

class MultiSelectStep(SelectStep):
    hint: str = '''\n\n* Press <Tab> to select the current line, Press <Enter> to continue.
* Press <Tab> on the selected line to unselect.
* <Up> and <Down> are available how to move the current line.
* You can search for entries. Let's try typing some words! ^_^
* If you have not selected any, you can also press <Enter> to select the current line and continue.

TODO: hint: You can use some key combinations.
    <Ctrl-P>: Prevous screen
    <Ctrl-C>: Exit'''
    name: str = 'Select choices'

    def main(self, environment: Environment, choices: List[str]) -> None:
        self.fzf_options += ['--multi']
        super().main(environment, choices)
