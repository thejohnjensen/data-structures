"""Test Module for hash table.."""
from hash_table import HashTable
import pytest


with open('/usr/share/dict/words', 'r') as word_list:
    words = word_list.read().split('\n')[::100]


@pytest.fixture
def ht_additive():
    """Build fixture with additive algo."""
    h_a = HashTable(1024, 0)
    for word in words:
        h_a.set(word, word)
    return h_a


@pytest.fixture
def ht_bernstein():
    """Build fixture with bernstein algo."""
    h_b = HashTable(1024, 1)
    for word in words:
        h_b.set(word, word)
    return h_b


def test_additive_algorithm(ht_additive):
    """Test hash table with add algo gets correct val."""
    for word in words:
        get_word_from_ht = ht_additive.get(word)
        assert word == get_word_from_ht


def test_bernstein_algorithm(ht_bernstein):
    """Test hash table with bern algo gets correct val."""
    for word in words:
        get_word_from_ht = ht_bernstein.get(word)
        assert word == get_word_from_ht


def test_error_if_key_not_str(ht_additive):
    """Test that key cannot be int."""
    with pytest.raises(TypeError):
        ht_additive.set(88, 'hi')


def test_error_if_algo_not_0_or_1():
    """Test that init raises proper error."""
    with pytest.raises(ValueError):
        HashTable(10, 8)
