from ..command import Command
from ..environment import Environment
from ..step import Step

class SynchronizeNtp(Step):
    description: str = 'Synchronizing system clock from NTP server...'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        Command.run(['timedatectl', 'set-ntp', 'true'])
