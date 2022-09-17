from muos import (
    Boot,
    Disk,
    DiskFormat,
    Environment,
    FileSystem,
    FstabTag,
    Partition,
    Runner,
    System,
    User,
)

from muos.etc import (
    Etc,
    Fstab,
    LocaleConf,
    VconsoleConf,
)

from muos.steps import (
    Begin,
    SynchronizeNtp,
    ProcessDisk,
    BootstrapArchLinux,
    ProcessSystem,
)

from muos.steps.arch_chroot import (
    InstallGrub,
    MakeBootx64Efi,
    InstallNetworkManager,
    EnableSystemdServices,
)

environment = Environment(
    boot=Boot(
        efi='grubx64.efi',
        id='grub',
    ),
    disk=Disk(
        format=DiskFormat.GPT,
        mountpoint='/mnt',
        name='/dev/sda',
        partitions=[
            Partition(
                filesystem=FileSystem.EXT4,
                mountpoint='/',
                size='100%',
                type='Linux root (x86-64)',
            ),
            Partition(
                filesystem=FileSystem.FAT32,
                mountpoint='/boot',
                size='300MiB',
                type='EFI System',
            ),
        ],
    ),
    etc=Etc(
        fstab=Fstab(
            tag=FstabTag.UUID,
        ),
        hostname='muos',
        locale_conf=LocaleConf(
            lang='en_US.UTF-8',
        ),
        vconsole_conf=VconsoleConf(
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
    system=System(
        locales=[
            'en_US.UTF-8 UTF-8',
        ],
        timezone='UTC',
    ),
    users=[
        User(
            name='root',
            password='toor',
        ),
    ],
)

runner = Runner(
    environment=environment,
    steps=[
        Begin(),
        SynchronizeNtp(),
        ProcessDisk(),
        BootstrapArchLinux(),
        ProcessSystem(),
        InstallGrub(),
        MakeBootx64Efi(),
        InstallNetworkManager(),
        EnableSystemdServices(),
    ],
)

runner.run()
