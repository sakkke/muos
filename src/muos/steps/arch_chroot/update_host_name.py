from pathlib import Path
from ...environment import Environment
from ...lib import create_file
from ...step import Step

class UpdateHostName(Step):
    name: str = 'Update /etc/hostname'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        create_file(Path(environment.mnt) / 'etc' / 'hostname', [
            environment.host_name,
        ])
