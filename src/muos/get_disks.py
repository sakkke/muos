from subprocess import run
from typing import List

def get_disks() -> List[str]:
    disks: List[str] = []
    sfdisk = run(['sfdisk', '--list'], capture_output=True, text=True)

    for line in sfdisk.stdout.split('\n'):
        if not line.startswith('Disk /'):
            continue

        tokens = line.split(' ')

        disk = tokens[1][:-1]

        disks.append(disk)

    return disks
