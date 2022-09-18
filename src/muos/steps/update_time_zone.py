from pathlib import Path
from ..environment import Environment
from ..step import Step

class UpdateTimeZone(Step):
    name: str = 'Updating a time zone...'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        localtime = Path(environment.mnt) / 'etc' / 'localtime'
        timezone = Path('/usr/share/zoneinfo/{}'.format(environment.time_zone))
        localtime.symlink_to(timezone)
