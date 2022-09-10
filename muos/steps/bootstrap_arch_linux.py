from pathlib import Path
from shutil import copy
from tempfile import mkdtemp
from ..command import Command
from ..environment import Environment
from ..step import Step

class BootstrapArchLinux(Step):
    description: str = 'Bootstrapping Arch Linux...'

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

        Command.run(['pacstrap', '-C', pacman_conf, environment.mnt] + environment.pacstrap_packages)
