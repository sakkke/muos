from ..environment import Environment
from ..get_disks import get_disks
from ..step import Step

class SelectDisk(Step):
    name: str = 'Selecting a disk...'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        choices = get_disks()
        result = environment.fzf.prompt(choices, '--height=10 --layout=reverse')
        environment.disk = result[0]
