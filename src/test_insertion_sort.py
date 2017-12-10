"""."""
from insertion_sort import insertion
from random import randint
import pytest


def test_insertion():
    """Test with random list."""
    unsorted = [randint(0, 1000000) for i in range(1000)]
    assert insertion(unsorted) == sorted(unsorted)


def test_insertion_worse_case():
    """Test with reversed list."""
    reverse = [i for i in range(1000)]
    reverse.reverse()
    assert insertion(reverse) == sorted(reverse)


def test_insertion_passed_a_string():
    """Test that raises error."""
    with pytest.raises(TypeError):
        assert insertion('hello')


def test_insertion_empty_list():
    """Test that properly handles an empty list."""
    assert insertion([]) == []


def test_insertion_in_order():
    """Test doesn't mess with my list when in order."""
    in_order = [i for i in range(1000)]
    assert insertion(in_order) == in_order