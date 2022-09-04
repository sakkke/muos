from ..command import Command
from ..step import Step

class SynchronizeNtp(Step):
    name: str = 'Synchronize NTP'

    def main(self) -> None:
        Command.run(['timedatectl', 'set-ntp', 'true'])
