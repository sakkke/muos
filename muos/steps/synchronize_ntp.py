from subprocess import run
from ..step import Step

class SynchronizeNtp(Step):
    name: str = 'Synchronize NTP'

    def main(self) -> None:
        run(['timedatectl', 'set-ntp', 'true'])
