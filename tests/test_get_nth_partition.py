from muos.get_nth_partition import get_nth_partition

def test_get_nth_partition():
    assert get_nth_partition('/dev/sda', 1) == '/dev/sda1'
