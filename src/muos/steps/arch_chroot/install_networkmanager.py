from ...command import Command
from ...environment import Environment
from ...step import Step

class InstallNetworkManager(Step):
    name: str = 'Installing NetworkManager...'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        packages = [
            'networkmanager',
        ]
        Command.run(['arch-chroot', environment.mnt, 'pacman', '--noconfirm', '--sync'] + packages)
        environment.systemd_services += ['NetworkManager.service']
