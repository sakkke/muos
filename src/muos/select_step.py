from typing import List
from .environment import Environment
from .step import Step

class SelectStep(Step):
    choices: List
    fzf_options: List[str] = [
        '--height=80%',
        '--info=inline',
        '--layout=reverse',
        '--pointer="*"',
        '--prompt=">>> "',
    ]
    hint: str = '''\n\n* Press <Enter> to select the current line and continue.
* <Up> and <Down> are available how to move the current line.
* You can search for entries. Let's try typing some words! ^_^

TODO: hint: You can use some key combinations.
    <Ctrl-P>: Prevous screen
    <Ctrl-C>: Exit'''
    name: str = 'Select a choice'

    def main(self, environment: Environment, choices: List[str]) -> None:
        super().main(environment)
        self.choices = environment.fzf.prompt(choices, ' '.join(self.fzf_options + ['--header="{}{}"'.format(self.name, self.hint)]))
