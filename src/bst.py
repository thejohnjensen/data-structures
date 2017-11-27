"""Module for creating binary search tree."""
import timeit


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
        After insert this function will update parent nodes with a depth value.

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
            return self.root.left.depth - self.root.right.depth
        elif self.root.right:
            return -(self.root.right.depth + 1)
        elif self.root.left:
            return self.root.left.depth + 1

    def in_order(self):
        """Traverse the left subtree, visit root, then traverse the right."""
        nodes = []
        current = self.root
        if current is None:
            raise ValueError("The bst is empty.")

        def _recur_in_order(current):
            """Recursively get tree nodes starting down the left."""
            if current.left is None or current.left.val in nodes:
                if current.val not in nodes:
                    nodes.append(current.val)
                if current.right and current.right.val not in nodes:
                    _recur_in_order(current.right)
                if current.parent:
                    _recur_in_order(current.parent)
                return
            _recur_in_order(current.left)

        _recur_in_order(current)
        return nodes

    def pre_order(self):
        """
        Traversal through bst starting at root and going left.

        Pre order looks at the nodes value when it first passes it.
        """
        nodes = []
        current = self.root
        if current is None:
            raise ValueError("The bst is empty.")

        def _recur_pre_order(current):
            """Recursive helper function for pre-order traversal."""
            if current:
                if current.val not in nodes:
                    nodes.append(current.val)
                if current.left and current.left.val not in nodes:
                    return _recur_pre_order(current.left)
                elif current.right and current.right.val not in nodes:
                    return _recur_pre_order(current.right)
                else:
                    return _recur_pre_order(current.parent)
        _recur_pre_order(current)
        return nodes

    def post_order(self):
        """
        Traversal through bst starting at root and going left.

        Post order will look at all leaves before looking at sub trees.
        """
        nodes = []
        current = self.root
        if current is None:
            raise ValueError("The bst is empty.")

        def _recur_post_order(current):
            """Recursive helper function for post-order traversal."""
            if current:
                if current.left and current.left.val not in nodes:
                    return _recur_post_order(current.left)
                elif current.right and current.right.val not in nodes:
                    return _recur_post_order(current.right)
                nodes.append(current.val)
                return _recur_post_order(current.parent)
        _recur_post_order(current)
        return nodes

    def breadth_first(self):
        """
        Traversal through bst with breadth first approach.

        Look at each node at current depth before going on to next level.
        """
        from que_ import Queue
        q = Queue()
        nodes = []
        q.enqueue(self.root)
        if self.root is None:
            raise ValueError("The bst is empty.")

        def _recur_breadth_first():
            """"Recursive helper function for breadth first."""
            try:
                current = q.dequeue()
                nodes.append(current.val)
                if current.left:
                    q.enqueue(current.left)
                if current.right:
                    q.enqueue(current.right)
                _recur_breadth_first()
            except IndexError:
                return
        _recur_breadth_first()
        return nodes


if __name__ == '__main__':
    bst = BST()
    bst.insert(8)
    bst.insert(4)
    bst.insert(12)
    bst.insert(6)
    bst.insert(13)
    bst.insert(11)
    bst.insert(9)
    bst.insert(0)
    bst.insert(3)
    bst.insert(100)
    print(timeit.timeit("bst.search(100)", setup="from __main__ import bst"))
