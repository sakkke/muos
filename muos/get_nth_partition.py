def get_nth_partition(disk: str, n: int) -> str:
    if disk.startswith('/dev/loop'):
        return '{}p{}'.format(disk, n)

    if disk.startswith('/dev/mmcblk'):
        return '{}p{}'.format(disk, n)

    if disk.startswith('/dev/nvme'):
        return '{}p{}'.format(disk, n)

    return '{}{}'.format(disk, n)
