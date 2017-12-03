"""Test Module for Trie."""
from trie import Trie


with open('/usr/share/dict/words', 'r') as word_list:
    words = word_list.read().split('\n')[::100]


def test_insert_trie():
    """Test chaining words."""
    t = Trie()
    t.insert('at')
    t.insert('attic')
    assert 'a' in t.root.children
    assert 't' in t.root.children['a'].children
    assert t.root.children['a'].children['t'].data == 'at'
    assert 't' in t.root.children['a'].children['t'].children
    assert 'i' in t.root.children['a'].children['t'].children['t'].children
    assert 'c' in t.root.children['a'].children['t'].children['t'].children['i'].children
    assert t.root.children['a'].children['t'].children['t'].children['i'].children['c'].data == 'attic'
    assert t.root.children['a'].data is None


def test_insert_contains_and_size():
    """Test insert, size and contains on many words."""
    t = Trie()
    num_words = 0
    for word in words:
        t.insert(word)
        num_words += 1
    for word in words:
        assert t.contains(word)
    assert t.size() == num_words


def test_remove_word():
    """Test removing many words from trie."""
    t = Trie()
    for word in words:
        t.insert(word)
    for word in words:
        t.remove(word)
    for word in words:
        assert not t.contains(word)
    assert t.size() == 0


def test_add_same_word_then_remove():
    """Test that adding the same word just overides the data."""
    t = Trie()
    t.insert('at')
    t.insert('at')
    assert t.contains('at')
    t.remove('at')
    assert not t.contains('at')
