"""Test Module for Trie."""
from trie import Trie
import pytest

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


def test_traverse_simple():
    """Test traverse method."""
    t = Trie()
    t.insert('water')
    t.insert('wash')
    gen = t.traverse('wa')
    trie_words = []
    for _ in range(2):
        trie_words.append(next(gen))
    assert trie_words == ['water', 'wash']


def test_traverse_big_start_with_ap():
    """Test traverse method."""
    t = Trie()
    match_words = []
    trie_words = []
    for word in words:
        t.insert(word)
        if word[:2] == 'ap':
            match_words.append(word)
    gen = t.traverse('ap')
    for _ in range(len(match_words)):
        trie_words.append(next(gen))
    assert trie_words == match_words


def test_traverse_big_start_with_wat():
    """Test traverse method."""
    t = Trie()
    match_words = []
    trie_words = []
    for word in words:
        t.insert(word)
        if word[:3] == 'wat':
            match_words.append(word)
    gen = t.traverse('wat')
    for _ in range(len(match_words)):
        trie_words.append(next(gen))
    assert trie_words == match_words


def test_traverse_big_start_no_start():
    """Test traverse method."""
    t = Trie()
    trie_words = []
    for word in words:
        t.insert(word)
    gen = t.traverse()
    for _ in range(len(words)):
        trie_words.append(next(gen))
    for word in trie_words:
        assert word in words


def test_error_no_string_insert():
    """Raise error when try to insert a non string."""
    t = Trie()
    with pytest.raises(TypeError):
        assert t.insert(99)


def test_error_no_string_contains():
    """Raise error when try to run contains on non string."""
    t = Trie()
    with pytest.raises(TypeError):
        assert t.contains(99)


def test_error_no_string_remove():
    """Raise error when try to run remove on non string."""
    t = Trie()
    with pytest.raises(TypeError):
        assert t.remove(99)
