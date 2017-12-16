"""Module for creating binary search tree."""
import timeit


class Node(object):
    """Node for binary search tree."""

    def __init__(self, val, parent=None, left=None, right=None):
        """Initialize Node with the following params."""
        self.depth = 0
        self.balance = 0
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
        current = self.root
        if current is None:
            raise ValueError("The bst is empty.")

        def _recur_in_order(current):
            """Recursively get tree nodes starting down the left."""
            if current:
                for val in _recur_in_order(current.left):
                    yield val
                yield current.val
                for val in _recur_in_order(current.right):
                    yield val
        return _recur_in_order(current)

    def pre_order(self):
        """
        Traversal through bst starting at root and going left.

        Pre order looks at the nodes value when it first passes it.
        """
        current = self.root
        if current is None:
            raise ValueError("The bst is empty.")

        def _recur_pre_order(current):
            """Recursive helper function for pre-order traversal."""
            if current:
                yield current.val
                for val in _recur_pre_order(current.left):
                    yield val
                for val in _recur_pre_order(current.right):
                    yield val
        return _recur_pre_order(current)

    def post_order(self):
        """
        Traversal through bst starting at root and going left.

        Post order will look at all leaves before looking at sub trees.
        """
        current = self.root
        if current is None:
            raise ValueError("The bst is empty.")

        def _recur_post_order(current):
            """Recursive helper function for post-order traversal."""
            if current:
                for val in _recur_post_order(current.left):
                        yield val
                for val in _recur_post_order(current.right):
                        yield val
                yield current.val
        return _recur_post_order(current)

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
            """Recursive helper function for breadth first."""
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
        for val in nodes:
            yield val

    def delete(self, val):
        """Method to delete a node that calls helper functions."""
        node = self.search(val)

        if node.left and node.right:
            return self._delete_node_with_two_children(node)
        elif node.left or node.right:
            return self._delete_node_with_one_child(node)
        else:
            return self._delete_node_with_no_chlidren(node)

    def _delete_node_with_no_chlidren(self, node):
        """Function to delete a node with no children."""
        if node.parent is None:
            self.root = None
        elif node.val > node.parent.val:
            node.parent.right = None
            node.parent = None
        else:
            node.parent.left = None
            node.parent = None

    def _delete_node_with_one_child(self, node):
        """Funciton to delete node with one child."""
        if node.parent is None:
            if node.left:
                self.root = node.left
                node.left = None
                self.root.parent = None
            else:
                self.root = node.right
                node.right = None
                self.root.parent = None
        elif node.val < node.parent.val:
            if node.left:
                node.left.parent = node.parent
                node.parent.left = node.left
            else:
                node.right.parent = node.parent
                node.parent.left = node.right
        else:
            if node.left:
                node.left.parent = node.parent
                node.parent.right = node.left
            else:
                node.right.parent = node.parent
                node.parent.right = node.right

    def _delete_node_with_two_children(self, node):
        """Function to delete node with two children."""
        new_node = self._get_node_to_swap(node)
        if node.parent is None:
            if new_node is node.left:
                node.right.parent = node.left
                node.left.right = node.right
                node.left.parent = None
                self.root = node.left
                node.right = None
                node.left = None
            else:
                if new_node.left:
                    new_node.parent.right = new_node.left
                    new_node.left.parent = new_node.parent
                    new_node.left = None
                    new_node.parent = None
                elif new_node.right:
                    new_node.parent.left = new_node.right
                    new_node.right.parent = new_node.parent
                    new_node.right = None
                    new_node.parent = None
                node.right.parent = new_node
                node.left.parent = new_node
                new_node.parent = node.parent
                new_node.left = node.left
                new_node.right = node.right
                self.root = new_node

        elif node.val < node.parent.val:
            new_node = self._get_node_to_swap(node)
            if new_node is node.left:
                node.parent.left = new_node
                node.right.parent = new_node
                new_node.parent = node.parent
                new_node.right = node.right
                node.parent = None
                node.right = None
                node.left = None
            else:
                if new_node.left:
                    new_node.parent.right = new_node.left
                    new_node.left.parent = new_node.parent
                    new_node.left = None
                    new_node.parent = None
                elif new_node.right:
                    new_node.parent.left = new_node.right
                    new_node.right.parent = new_node.parent
                    new_node.right = None
                    new_node.parent = None
                node.right.parent = new_node
                node.left.parent = new_node
                node.parent.left = new_node
                new_node.parent = node.parent
                new_node.left = node.left
                new_node.right = node.right

        else:
            new_node = self._get_node_to_swap(node)
            if new_node is node.left:
                node.parent.right = new_node
                node.right.parent = new_node
                new_node.parent = node.parent
                new_node.right = node.right
                node.parent = None
                node.right = None
                node.left = None
            else:
                if new_node.left:
                    new_node.parent.right = new_node.left
                    new_node.left.parent = new_node.parent
                    new_node.left = None
                    new_node.parent = None
                elif new_node.right:
                    new_node.parent.left = new_node.right
                    new_node.right.parent = new_node.parent
                    new_node.right = None
                    new_node.parent = None
                node.right.parent = new_node
                node.left.parent = new_node
                node.parent.right = new_node
                new_node.parent = node.parent
                new_node.left = node.left
                new_node.right = node.right

    def _get_node_to_swap(self, node):
        """
        Get the deepest right node on the left sub tree or left most on.

        the right sub tree.
        """
        left_depth = 0
        right_depth = 0

        if node.left.right:
            current = node.left
            while current.right:
                left_depth += 1
                current = current.right

        if node.right.left:
            current = node.right
            while current.left:
                right_depth += 1
                current = current.left

        if left_depth >= right_depth:
            if left_depth == 0:
                return node.left
            else:
                current = node.left
                while current.right:
                    current = current.right
                return current
        else:
            current = node.right
            while current.left:
                current = current.left
            return current

    def max_depth(self):
        curr = self.root
        def _helper(curr):
            if self.root is None:
                return 0
            max_d_left = _helper(curr.left)
            max_d_right = _helper(curr.right)
            # import pdb; pdb.set_trace()
            if max_d_left > max_d_right:
                return max_d_left + 1
            else:
                return max_d_right + 1
        return _helper(curr)

            


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
