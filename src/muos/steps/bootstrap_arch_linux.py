from pathlib import Path
from shutil import copy
from tempfile import mkdtemp
from ..environment import Environment
from ..pacman import Pacman
from ..step import Step

class BootstrapArchLinux(Step):
    name: str = 'Bootstrap Arch Linux'

    def main(self, environment: Environment) -> None:
        super().main(environment)

        temp_d = mkdtemp()

        mirrorlist = Path(temp_d) / 'mirrorlist'

        for pacman_mirror in environment.pacman_mirrors:
            with mirrorlist.open('a') as f:
                f.write('Server = {}\n'.format(pacman_mirror))

        pacman_conf = Path(temp_d) / 'pacman.conf'

        source = Path(__file__).parent.parent / 'static' / 'pacman.conf'
        copy(source, pacman_conf)

        content = pacman_conf.read_text()
        replaced = content.replace('/etc/pacman.d/mirrorlist', str(mirrorlist))
        pacman_conf.write_text(replaced)

        pacman = Pacman()
        pacman.bootstrap(environment.mnt, environment.pacstrap_packages, options=['-C', pacman_conf])
