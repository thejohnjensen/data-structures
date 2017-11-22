"""Module for creating binary search tree."""


class Node(object):
    """Node for binary search tree."""

    def __init__(self, val, parent=None, left=None, right=None):
        """."""
        self.depth = 0
        self.parent = parent
        self.left = left
        self.right = right
        self.val = val


class BST(object):
    """Create a binary search tree object."""

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
            depth_count = 0
            while current:
                depth_count += 1
                if val == current.val:
                    raise ValueError("Value already exists in tree.")
                if val < current.val:
                    if current.left is None:
                        current.left = Node(val, current)
                        self._count += 1
                        # current.parent.depth += 1
                        if depth_count > self.root.depth:
                            self.root.depth = depth_count
                        break
                    else:
                        current = current.left
                        # current.parent.depth += 1
                elif val > current.val:
                    if current.right is None:
                        current.right = Node(val, current)
                        self._count += 1
                        # current.parent.depth += 1
                        if depth_count > self.root.depth:
                            self.root.depth = depth_count
                        break
                    else:
                        current = current.right
                        # current.parent.depth += 1

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
        """."""


