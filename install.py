#!/usr/bin/env python3

import muos
import muos.steps as steps
import muos.steps.arch_chroot as arch_chroot

environment = muos.Environment(
    bootloader_id='GRUB',
    bootx64_efi='<efi_dir>/EFI/<bootloader_id>/grubx64.efi',
    name='Install muOS',
    disk_format=muos.DiskFormat.GPT,
    file_systems=[
        muos.FileSystem.FAT32,
        muos.FileSystem.EXT4,
    ],
    fstab_tag=muos.FstabTag.UUID,
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

runner = muos.Runner(environment, [
    steps.Begin(),
    steps.SelectKeymap(),
    steps.LoadKeymap(),
    steps.SelectDisk(),
    steps.SelectPacmanMirrors(),
    steps.SelectTimeZone(),
    steps.SelectLocales(),
    steps.SelectMainLocale(),
    steps.SynchronizeNtp(),
    steps.FormatDisk(),
    steps.PartitionDisk(),
    steps.FormatPartitions(),
    steps.MountPartitions(),
    steps.BootstrapArchLinux(),
    steps.GenerateFstab(),
    steps.UpdateTimeZone(),
    arch_chroot.GenerateAdjtime(),
    arch_chroot.UpdateLocaleGen(),
    arch_chroot.GenerateLocales(),
    arch_chroot.UpdateLocaleConf(),
    arch_chroot.UpdateVconsoleConf(),
    arch_chroot.UpdateHostName(),
    arch_chroot.UpdatePasswords(),
    arch_chroot.InstallGrub(),
    arch_chroot.MakeBootx64Efi(),
    arch_chroot.InstallNetworkManager(),
    arch_chroot.EnableSystemdServices(),
])

runner.run()
