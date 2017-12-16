"""Test module for merge_sort."""
from merge_sort import merge_sort
from random import randint
import pytest


def test_merge_sort():
    """Test with random list."""
    unsorted = [randint(0, 1000000) for i in range(1000)]
    assert merge_sort(unsorted) == sorted(unsorted)


def test_merge_sort_worse_case():
    """Test with reversed list."""
    reverse = [i for i in range(1000)]
    reverse.reverse()
    assert merge_sort(reverse) == sorted(reverse)


def test_merge_sort_passed_a_string():
    """Test raises error when passed string."""
    with pytest.raises(TypeError):
        assert merge_sort('hello')


def test_merge_sort_empty_list():
    """Test properly handles an empty list."""
    assert merge_sort([]) == []


def test_merge_sort_in_order():
    """Test doesn't mess with my list when in order."""
    in_order = [i for i in range(1000)]
    assert merge_sort(in_order) == in_order
