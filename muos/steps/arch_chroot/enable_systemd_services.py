from ...command import Command
from ...environment import Environment
from ...step import Step

class EnableSystemdServices(Step):
    description: str = 'Enabling systemd services...'

    def main(self, environment: Environment) -> None:
        super().main(environment)

        for systemd_service in environment.systemd_services:
            Command.run(['arch-chroot', environment.mnt, 'systemctl', 'enable', systemd_service])
