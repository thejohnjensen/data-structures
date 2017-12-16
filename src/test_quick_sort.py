"""Test for quicksort."""
from quick_sort import quicksort
from random import randint
import pytest


def test_quicksort():
    """Test with random list."""
    unsorted = [randint(0, 1000000) for i in range(100)]
    assert quicksort(unsorted) == sorted(unsorted)


def test_quicksort_worse_case():
    """Test with reversed list."""
    reverse = [i for i in range(100)]
    reverse.reverse()
    assert quicksort(reverse) == sorted(reverse)


def test_quicksort_passed_a_string():
    """Test that raises error."""
    with pytest.raises(TypeError):
        assert quicksort('hello')


def test_quicksort_empty_list():
    """Test that properly handles an empty list."""
    assert quicksort([]) == []


def test_quicksort_in_order():
    """Test doesn't mess with my list when in order."""
    in_order = [i for i in range(100)]
    assert quicksort(in_order) == in_order