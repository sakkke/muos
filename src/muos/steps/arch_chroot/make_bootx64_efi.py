from pathlib import Path
from shutil import copy
from ...environment import Environment
from ...get_efi_dir import get_efi_dir
from ...step import Step

class MakeBootx64Efi(Step):
    name: str = 'Making <efi_dir>/EFI/boot/bootx64.efi...'

    def main(self, environment: Environment) -> None:
        super().main(environment)
        efi_dir = get_efi_dir(environment)
        boot = Path('{}{}/boot'.format(environment.mnt, str(efi_dir)))
        boot.mkdir(exist_ok=True)
        bootx64_efi = str(Path('{}{}'.format(environment.mnt, str(environment.bootx64_efi))))
        bootx64_efi = bootx64_efi.replace('<bootloader_id>', environment.bootloader_id)
        bootx64_efi = bootx64_efi.replace('<efi_dir>', str(efi_dir))
        copy(bootx64_efi, efi_dir)
