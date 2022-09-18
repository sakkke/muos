from ...environment import Environment
from ...pacman import Pacman
from ...step import Step

class InstallNetworkManager(Step):
    name: str = 'Install NetworkManager'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        pacman = Pacman()
        pacman.add(environment.mnt, ['networkmanager'])
        environment.systemd_services += ['NetworkManager.service']
