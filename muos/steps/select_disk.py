from ..environment import Environment
from ..get_disks import get_disks
from ..step import Step

class SelectDisk(Step):
    name: str = 'Select a disk'

    def main(self, environment: Environment) -> None:
        choices = get_disks()
        result = environment.fzf.prompt(choices, '--height=50% --layout=reverse')
        environment.disk = result[0]