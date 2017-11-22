"""Module for creating binary search tree."""


class Node(object):
    """Node for binary search tree."""

    def __init__(self, val, parent=None, left=None, right=None):
        """Initialize Node with the following params."""
        self.depth = 0
        self.parent = parent
        self.left = left
        self.right = right
        self.val = val


class BST(object):
    """Create a binary search tree object."""

    def __init__(self, iterable=None):
        """Initialize BST with following params."""
        self.root = None
        self._count = 0
        if isinstance(iterable, (list, tuple)):
            for val in iterable:
                self.insert(val)

    def insert(self, val):
        """Insert node into tree with val as value."""
        if self._count == 0:
            self.root = Node(val)
            self._count += 1
        else:
            current = self.root
            while current:
                if val == current.val:
                    raise ValueError("Value already exists in tree.")
                if val < current.val:
                    if current.left is None:
                        current.left = Node(val, current)
                        self._count += 1
                        self._set_depth(current.left)
                        break
                    else:
                        current = current.left
                elif val > current.val:
                    if current.right is None:
                        current.right = Node(val, current)
                        self._count += 1
                        self._set_depth(current.right)
                        break
                    else:
                        current = current.right

    def _set_depth(self, current):
        """
        After each insert this function will update parent nodes with a depth value.

        The depth value signifies the depth below the current node.
        """
        if current.parent is None:
            return
        else:
            if current.depth + 1 > current.parent.depth:
                current.parent.depth = current.depth + 1
            return self._set_depth(current.parent)

    def search(self, val):
        """Search the bst for val, return the node if in the bst else None."""
        current = self.root
        return self._search_recur(val, current)

    def _search_recur(self, val, current):
        """Helper function to recursively search BST."""
        if current is None:
            return None
        elif val == current.val:
            return current
        elif val > current.val:
            current = current.right
            return self._search_recur(val, current)
        else:
            current = current.left
            return self._search_recur(val, current)

    def size(self):
        """Return the size, # of nodes of bst."""
        return self._count

    def depth(self):
        """Return the depth of the tree."""
        return self.root.depth

    def contains(self, val):
        """Return true if val in BST else False."""
        current = self.root
        return True if self._search_recur(val, current) else False

    def balance(self):
        """
        Return an integer depicting how well balanced the tree is.

        Deeper on the right == Negative.
        Deepter on the left == Positive.
        Balanced if +-1.
        """
        if self._count == 0:
            raise ValueError("The tree is empty")
        if self.root.right and self.root.left:
            return self.root.left.depth - self.root.right.depth  # delta does not need + 1
        elif self.root.right:
            return -(self.root.right.depth + 1)  # add one to count current node
        elif self.root.left:
            return self.root.left.depth + 1  # add one to count current node
