"""."""
from bst_balanced_4_4 import BST


def test_create_bst():
    """."""
    bst = BST()
    assert bst


def test_4_3_5_bst():
    """."""
    bst = BST()
    bst.insert(4)
    bst.insert(3)
    bst.insert(5)
    bst.insert(2)
    bst.insert(0)
    bst.insert(1)
    bst.insert(100)
    bst.insert(50)
    bst.insert(40)
    bst.insert(101)
    assert bst.root.data == 4
    assert bst.root.left.data == 3
    assert bst.root.right.data == 5
    assert bst.root.left.left.data == 2
    assert bst.root.left.left.left.data == 0
    assert bst.root.left.left.left.right.data == 1
    assert bst.root.right.right.right.data == 101
    assert bst.size == 10


def test_search():
    """."""
    bst = BST()
    bst.insert(4)
    bst.insert(3)
    bst.insert(5)
    bst.insert(2)
    bst.insert(0)
    bst.insert(1)
    bst.insert(100)
    bst.insert(50)
    bst.insert(40)
    bst.insert(101)
    assert bst.search(4) is True
    assert bst.search(3) is True
    assert bst.search(5) is True
    assert bst.search(101) is True
    assert bst.search(1) is True
    assert bst.search(10) is False
    assert bst.search(-1) is False


def test_bfs():
    """."""
    bst = BST()
    bst.insert(4)
    bst.insert(3)
    bst.insert(5)
    bst.insert(2)
    bst.insert(0)
    bst.insert(1)
    bst.insert(100)
    bst.insert(50)
    bst.insert(40)
    bst.insert(101)
    assert bst.bfs() == [4, 3, 5, 2, 100, 0, 50, 101, 1, 40]


def test_pre_order():
    """."""
    bst = BST()
    bst.insert(4)
    bst.insert(3)
    bst.insert(5)
    bst.insert(2)
    bst.insert(0)
    bst.insert(1)
    bst.insert(100)
    bst.insert(50)
    bst.insert(40)
    bst.insert(101)
    assert bst.pre_order() == [4, 3, 2, 0, 1, 5, 100, 50, 40, 101]


def test_in_order():
    """."""
    bst = BST()
    bst.insert(4)
    bst.insert(3)
    bst.insert(5)
    bst.insert(2)
    bst.insert(0)
    bst.insert(1)
    bst.insert(100)
    bst.insert(50)
    bst.insert(40)
    bst.insert(101)
    assert bst.in_order() == [0, 1, 2, 3, 4, 5, 40, 50, 100, 101]


# def test_post_order():
#     """."""
#     bst = BST()
#     bst.insert(4)
#     bst.insert(3)
#     bst.insert(5)
#     bst.insert(2)
#     bst.insert(0)
#     bst.insert(1)
#     bst.insert(100)
#     bst.insert(50)
#     bst.insert(40)
#     bst.insert(101)
#     assert bst.post_order() == [1, 0, 2, 3, 40, 50, 101, 100, 5, 4]
