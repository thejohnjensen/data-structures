"""Test module for bubble sort."""
from random import randint
import pytest
from bubble_sort import bubble_sort


def test_bubble_sort():
    """Test bubble sort with random list."""
    unsorted = [randint(0, 1000000) for i in range(1000)]
    assert bubble_sort(unsorted) == sorted(unsorted)


def test_bubble_sort_worse_case():
    """Test bbs with reversed list."""
    reverse = [i for i in range(1000)]
    reverse.reverse()
    assert bubble_sort(reverse) == sorted(reverse)


def test_bubble_sort_passed_a_string():
    """Test that bbs raises error."""
    with pytest.raises(TypeError):
        assert bubble_sort('hello bulbasaur')


def test_bubble_sort_empty_list():
    """Test that bbs properly handles an empty list."""
    assert bubble_sort([]) == []


def test_bubble_sort_in_order():
    """Test bbs doesn't mess with my list when in order."""
    in_order = [i for i in range(1000)]
    assert bubble_sort(in_order) == in_order
