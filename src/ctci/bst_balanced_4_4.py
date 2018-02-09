"""Rewrite BST for practice and then write a function to check if balanced."""


class Node:
    """."""

    def __init__(self, data):
        """."""
        self.data = data
        self.left = None
        self.right = None


class BST:
    """."""

    def __init__(self):
        """."""
        self.root = None
        self.size = 0

    def insert(self, data, root=None):
        """."""
        if self.root is None:
            self.root = Node(data)
            self.size += 1
        else:
            if root is None:
                self.insert(data, self.root)
            else:
                if data < root.data:
                    if root.left is None:
                        root.left = Node(data)
                        self.size += 1
                    else:
                        self.insert(data, root.left)
                elif data > root.data:
                    if root.right is None:
                        root.right = Node(data)
                        self.size += 1
                    else:
                        self.insert(data, root.right)

    def search(self, data, curr=None):
        """Return True if in tree, else False."""
        if self.root.data == data:
            return True
        else:
            if curr is None:
                return self.search(data, self.root)
            else:
                if data == curr.data:
                    return True
                if data < curr.data:
                    if curr.left is None:
                        return False
                    return self.search(data, curr.left)
                else:
                    if curr.right is None:
                        return False
                    return self.search(data, curr.right)

    def bfs(self):
        """."""
        this_level = [self.root]
        visited = []

        while this_level:
            next_level = []
            for node in this_level:
                if node.left and node.left not in visited:
                    next_level.append(node.left)
                if node.right and node.right not in visited:
                    next_level.append(node.right)
                visited.append(node.data)
                this_level = next_level
        return visited

    def pre_order(self, node=None, traversal=[]):
        """."""
        traversal = traversal
        if node is None:
            self.pre_order(self.root)
        else:
            traversal.append(node.data)
            if node.left:
                self.pre_order(node.left, traversal)
            if node.right:
                self.pre_order(node.right, traversal)
        return traversal

    def in_order(self, node=None, traversal=[]):
        """."""
        traversal = traversal
        if node is None:
            self.in_order(self.root)
        else:
            if node.left:
                self.in_order(node.left, traversal)
            traversal.append(node.data)
            if node.right:
                self.in_order(node.right, traversal)
        return traversal

    def post_order(self, node=None, traversal=[]):
        """."""
        traversal = traversal
        if node is None:
            self.post_order(self.root)
        else:
            if node.left:
                self.post_order(node.left, traversal)
            if node.right:
                self.post_order(node.right, traversal)
            traversal.append(node)
        return traversal


def check_balance(bst):
    """."""
    nodes = bst.post_order()
    for node in nodes:
        if node.left:
            left_height = max(node.left.left_height, node.left.right_height)
            node.left_height = left_height + 1
        else:
            node.left_height = 0
        if node.right:
            right_height = max(node.right.left_height, node.right.right_height)
            node.right_height = right_height + 1
        else:
            node.right_height = 0
    right = bst.root.right_height
    left = bst.root.left_height
    if abs(right - left) > 1:
        return False
    return True


def check_if_bst(bst):
    """."""
    que = [bst.root]
    visited = []
    while que:
        curr = que.pop(0)
        if curr.left:
            if curr.left.data > curr.data:
                return False
            elif curr.left.data not in visited:
                que.append(curr.left)
        if curr.right:
            if curr.right.data < curr.data:
                return False
            elif curr.right.data not in visited:
                que.append(curr.right)
        visited.append(curr.data)
    return True


if __name__ == '__main__':
    bst = BST()
    bst.insert(3)
    bst.insert(2)
    bst.insert(1)
    bst.insert(4)
    bst.insert(5)
