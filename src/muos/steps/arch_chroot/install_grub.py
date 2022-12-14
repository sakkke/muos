from ...command import Command
from ...environment import Environment
from ...get_efi_dir import get_efi_dir
from ...pacman import Pacman
from ...step import Step

class InstallGrub(Step):
    name: str = 'Install GNU GRUB'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        pacman = Pacman()
        pacman.add(environment.mnt, ['efibootmgr', 'grub'])
        efi_dir = get_efi_dir(environment)
        Command.run([
            'arch-chroot', environment.mnt, 'grub-install',
            '--bootloader-id', environment.bootloader_id,
            '--efi-directory', efi_dir,
            '--target', 'x86_64-efi'
        ])
        Command.run([
            'arch-chroot', environment.mnt, 'grub-mkconfig',
            '--output', str(efi_dir / 'grub' / 'grub.cfg')
        ])
