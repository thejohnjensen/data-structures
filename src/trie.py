"""Trie Datastructure."""


class Node(object):
    """
    Node that holds data if the word is complete and.

    dictionary of all chaining letters.
    """

    def __init__(self, data=None):
        """Initialize Node with dictionarys."""
        self.data = data
        self.children = {}


class Trie(object):
    """Trie, made up of insert, contains, size, and remove methods."""

    def __init__(self):
        """Initialize trie."""
        self.root = Node()
        self.num_words = 0

    def insert(self, string):
        """Insert a new word into Trie."""
        if not isinstance(string, str):
            raise TypeError('Input must be a string.')
        current = self.root
        for ind, letter in enumerate(string):
            if letter in current.children:
                current = current.children[letter]
            else:
                current.children[letter] = Node()
                current = current.children[letter]
            if ind == len(string) - 1:
                current.data = string
        self.num_words += 1

    def contains(self, string):
        """Return True if string in Trie, else False."""
        if not isinstance(string, str):
            raise TypeError('Input must be a string.')
        contains = False
        current = self.root
        for ind, letter in enumerate(string):
            if letter in current.children:
                current = current.children[letter]
                if ind == len(string) - 1:
                    if current.data:
                        contains = True
        return contains

    def size(self):
        """Return number of words in Trie."""
        return self.num_words

    def remove(self, string):
        """Remvoe word from Trie."""
        if not isinstance(string, str):
            raise TypeError('Input must be a string.')
        contains = False
        current = self.root
        for ind, letter in enumerate(string):
            if letter in current.children:
                current = current.children[letter]
                if ind == len(string) - 1:
                    if current.data:
                        contains = True
                        current.data = None
                        self.num_words -= 1
        if contains is False:
            raise AttributeError('String is not in Trie.')

    def traverse(self, start=''):
        """Traverse trie and return a generator for all words in trie."""
        if not isinstance(start, str):
            raise TypeError('Input must be a string.')
        tokens = []
        current = self.root
        for letter in start:
            if letter in current.children:
                current = current.children[letter]
            else:
                yield tokens

        def _recursive(current):
            """Recursive helper for trie."""
            for child in current.children:
                if current.children[child].data:
                    tokens.append(current.children[child].data)
                _recursive(current.children[child])
        _recursive(current)
        for token in tokens:
            yield token



