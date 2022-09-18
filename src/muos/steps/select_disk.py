from ..environment import Environment
from ..get_disks import get_disks
from ..select_step import SelectStep

class SelectDisk(SelectStep):
    name: str = 'Select a disk'

    def main(self, environment: Environment) -> None:
        self.fzf_options += ['--preview="sfdisk --list {}"', '--preview-window=down:50%']
        super().main(environment, get_disks())
        environment.disk = self.choices[0]
