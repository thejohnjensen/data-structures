"""."""


class Node(object):
    """docstring for Node."""

    def __init__(self, val, parent=None, left=None, right=None):
        """."""
        self.parent = parent
        self.left = left
        self.right = right
        self.val = val


class BST(object):
    """."""

    def __init__(self):
        """."""
        self.root = None
        self._count = 0

    def insert(self, val):
        """."""
        if self._count == 0:
            self.root = Node(val)
            self._count += 1
        else:
            current = self.root
            while current:
                if val < current.val:
                    if current.left is None:
                        current.left = Node(val, current)
                        self._count += 1
                        break
                    else:
                        current = current.left
                elif val > current.val:
                    if current.right is None:
                        current.right = Node(val, current)
                        self._count += 1
                        break
                    else:
                        current = current.right

    def search(self, val):
        """."""

    def size(self):
        """."""
        return self._count

    def depth(self):
        """."""

    def contains(self, val):
        """."""

    def balance(self):
        """."""



a = BST()
a.insert(8)
a.insert(12)
a.insert(2)