"""Module to create hash table with two different algorithms."""


class HashTable(object):
    """Hash Table Class."""

    def __init__(self, size, hash_choice):
        """
        Initialize Hash Table.

        Hash input is 0 for additive hash or 1 for bernstein hash.
        """
        if hash_choice == 0 or hash_choice == 1:
            self.hash_algo = hash_choice
        else:
            raise ValueError('Input 0 for Additive or 1 for Bernstein hash.')
        self.table_size = size
        self.hash_table = [[] for _ in range(size)]

    def set(self, key, val):
        """
        Set key value pair in hash table.

        If the key already exists the value is overwritten.
        """
        if not isinstance(key, str):
            raise TypeError('Key must be a string.')
        if self.hash_algo == 0:
            hash_val = self._hash_a(key)
        else:
            hash_val = self._hash_b(key)
        if len(self.hash_table[hash_val]) == 0:
            self.hash_table[hash_val].append([key, val])
        else:
            for bucket in self.hash_table[hash_val]:
                if bucket[0] == key:
                    bucket[1] = val
                    break
                self.hash_table[hash_val].append([key, val])

    def get(self, key):
        """Return the value associated with key."""
        if not isinstance(key, str):
            raise TypeError('Key must be a string.')
        if self.hash_algo == 0:
            hash_val = self._hash_a(key)
        else:
            hash_val = self._hash_b(key)
        for bucket in self.hash_table[hash_val]:
            if bucket[0] == key:
                return bucket[1]

    def _hash_a(self, key):
        """Additive hash."""
        hash_val = 0
        for i in key:
            hash_val += ord(i)
        return hash_val % self.table_size

    def _hash_b(self, key):
        """Bernstein hash."""
        hash_val = 0
        for i in key:
            hash_val = 33 * hash_val + ord(i)
        return hash_val % self.table_size
