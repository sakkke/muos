#!/usr/bin/env python3

from muos import (
    DiskFormat,
    Environment,
    FileSystem,
    FstabTag,
    Runner,
)

from muos.steps import (
    Begin,
    BootstrapArchLinux,
    FormatDisk,
    FormatPartitions,
    GenerateFstab,
    LoadKeymap,
    MountPartitions,
    PartitionDisk,
    SelectDisk,
    SelectKeymap,
    SelectLocales,
    SelectMainLocale,
    SelectPacmanMirrors,
    SelectTimeZone,
    SynchronizeNtp,
    UpdateTimeZone,
)

from muos.steps.arch_chroot import (
    EnableSystemdServices,
    GenerateAdjtime,
    GenerateLocales,
    InstallGrub,
    InstallNetworkManager,
    MakeBootx64Efi,
    UpdateHostName,
    UpdateLocaleGen,
    UpdatePasswords,
    UpdateVconsoleConf,
)

environment = Environment(
    bootloader_id='GRUB',
    bootx64_efi='<efi_dir>/EFI/<bootloader_id>/grubx64.efi',
    name='Installing muOS...',
    disk_format=DiskFormat.GPT,
    file_systems=[
        FileSystem.FAT32,
        FileSystem.EXT4,
    ],
    fstab_tag=FstabTag.UUID,
    host_name='muos',
    mnt = '/mnt',
    mount_points=[
        (2, '/'),
        (1, '/boot'),
    ],
    pacstrap_packages=[
        'base',
        'linux',
        'linux-firmware',
    ],
    partitions=[
        'size=300MiB, type="EFI System"',
        'type="Linux root (x86-64)"',
    ],
    passwords=[
        ('root', 'toor'),
    ],
)

runner = Runner(environment, [
    Begin(),
    SelectKeymap(),
    LoadKeymap(),
    SelectDisk(),
    SelectPacmanMirrors(),
    SelectTimeZone(),
    SelectLocales(),
    SelectMainLocale(),
    SynchronizeNtp(),
    FormatDisk(),
    PartitionDisk(),
    FormatPartitions(),
    MountPartitions(),
    BootstrapArchLinux(),
    GenerateFstab(),
    UpdateTimeZone(),
    GenerateAdjtime(),
    UpdateLocaleGen(),
    GenerateLocales(),
    UpdateVconsoleConf(),
    UpdateHostName(),
    UpdatePasswords(),
    InstallGrub(),
    MakeBootx64Efi(),
    InstallNetworkManager(),
    EnableSystemdServices(),
])

runner.run()
