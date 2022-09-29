import muos
import muos.etc as etc
import muos.steps as steps
import muos.steps.arch_chroot as arch_chroot

environment = muos.Environment(
    boot=muos.Boot(
        efi='grubx64.efi',
        id='grub',
    ),
    disk=muos.Disk(
        format=muos.DiskFormat.GPT,
        mountpoint='/mnt',
        partitions=[
            muos.Partition(
                filesystem=muos.FileSystem.EXT4,
                mountpoint='/',
                size='100%',
                type='Linux root (x86-64)',
            ),
            muos.Partition(
                filesystem=muos.FileSystem.FAT32,
                mountpoint='/boot',
                size='300MiB',
                type='EFI System',
            ),
        ],
        path='/dev/sda',
    ),
    etc=etc.Etc(
        fstab=etc.Fstab(
            tag=muos.FstabTag.UUID,
        ),
        hostname='muos',
        locale_conf=etc.LocaleConf(
            lang='en_US.UTF-8',
        ),
        vconsole_conf=etc.VconsoleConf(
            keymap='us',
        ),
    ),
    name='Install muOS',
    pacman_mirrors=[
        'https://geo.mirror.pkgbuild.com/$repo/os/$arch',
    ],
    pacstrap_packages=[
        'base',
        'linux',
        'linux-firmware',
    ],
    system=muos.System(
        locales=[
            'en_US.UTF-8 UTF-8',
        ],
        timezone='UTC',
    ),
    users=[
        muos.User(
            name='root',
            password='toor',
        ),
    ],
)

runner = muos.Runner(
    environment=environment,
    steps=[
        steps.Begin(),
        steps.SynchronizeNtp(),
        steps.ProcessDisk(),
        steps.BootstrapArchLinux(),
        steps.ProcessSystem(),
        arch_chroot.InstallGrub(),
        arch_chroot.MakeBootx64Efi(),
        arch_chroot.InstallNetworkManager(),
        arch_chroot.EnableSystemdServices(),
    ],
)

runner.run()
