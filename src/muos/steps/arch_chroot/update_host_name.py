from pathlib import Path
from ...environment import Environment
from ...step import Step

class UpdateHostName(Step):
    name: str = 'Updating /etc/hostname...'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        hostname = Path(environment.mnt) / 'etc' / 'hostname'
        hostname.write_text(environment.host_name)
