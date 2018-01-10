"""Test mod for radix sort."""

from radix_sort import radix_sort
from random import randint
import pytest


def test_insertion():
    """Test with random list."""
    unsorted = [randint(0, 1000000) for i in range(1000)]
    assert radix_sort(unsorted) == sorted(unsorted)


def test_radix_sort_worse_case():
    """Test with reversed list."""
    reverse = [i for i in range(1000)]
    reverse.reverse()
    assert radix_sort(reverse) == sorted(reverse)


def test_radix_sort_passed_a_string():
    """Test that raises error."""
    with pytest.raises(TypeError):
        assert radix_sort('hello')


def test_radix_sort_empty_list():
    """Test that properly handles an empty list."""
    assert radix_sort([]) == []


def test_radix_sort_in_order():
    """Test doesn't mess with my list when in order."""
    in_order = [i for i in range(1000)]
    assert radix_sort(in_order) == in_order
