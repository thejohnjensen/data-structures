"""."""


class Node(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BST(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert node into tree with data as value."""
        if self.root is None:
            self.root = Node(data)
        else:
            current = self.root
            while current:
                if data == current.data:
                    raise ValueError("Value already exists in tree.")
                if data < current.data:
                    if current.left is None:
                        current.left = Node(data)
                        break
                    else:
                        current = current.left
                elif data > current.data:
                    if current.right is None:
                        current.right = Node(data)
                        break
                    else:
                        current = current.right


if __name__ == '__main__':
    bst = BST()
    vals = [8,6,5,4,10,12]
    for i in vals:
        bst.insert(i)
