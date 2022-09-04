from subprocess import run
from ..step import Step

class SynchronizeNtp(Step):
    def main(self) -> None:
        run(['timedatectl', 'set-ntp', 'true'])
