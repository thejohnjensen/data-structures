"""Test mod for radix sort."""

from radix_sort import radix_sort


def test_radix_small():
    """."""
    test_list = radix_sort([5, 4, 3, 2, 1])
    assert test_list == [1, 2, 3, 4, 5]
