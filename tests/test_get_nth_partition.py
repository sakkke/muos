from muos.get_nth_partition import get_nth_partition

def test_get_nth_partition():
    assert get_nth_partition('/dev/sda', 1) == '/dev/sda1'

def test_loop0():
    assert get_nth_partition('/dev/loop0', 1) == '/dev/loop0p1'

def test_mmcblk0():
    assert get_nth_partition('/dev/mmcblk0', 1) == '/dev/mmcblk0p1'

def test_nvme0n1():
    assert get_nth_partition('/dev/nvme0n1', 1) == '/dev/nvme0n1p1'
