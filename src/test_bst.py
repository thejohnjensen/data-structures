"""Test module for the binary search tree."""
import pytest


def test_bst_exists(bst):
    """Test that fixture creates BST."""
    assert bst


def test_bst_root(bst):
    """Test that a root node is created."""
    bst.insert(8)
    assert bst.root.val == 8


def test_bst_root_child_none(bst):
    """Test that a root node is created with children set to None."""
    bst.insert(8)
    assert bst.root.left is None
    assert bst.root.right is None


def test_bst_three_nodes(bst):
    """Test a bst with root and a node on left and right."""
    bst.insert(8)
    bst.insert(4)
    bst.insert(12)
    assert bst.root.left.val == 4
    assert bst.root.right.val == 12


def test_insert_bst_full(bst_full):
    """Test that insert works for full BST."""
    assert bst_full.root.val == 8

    # Right Nodes
    assert bst_full.root.right.val == 12
    assert bst_full.root.right.right.val == 13
    assert bst_full.root.right.right.right.val == 100
    assert bst_full.root.right.left.val == 11
    assert bst_full.root.right.left.left.val == 9

    # Left Nodes
    assert bst_full.root.left.val == 4
    assert bst_full.root.left.left.val == 0
    assert bst_full.root.left.right.val == 6
    assert bst_full.root.left.left.right.val == 3


def test_bst_error_(bst):
    """Test a bst with root and a node on left and right."""
    bst.insert(8)
    with pytest.raises(ValueError):
            bst.insert(8)


def test_insert_bst_full_parents(bst_full):
    """Test that nodes have parent."""
    assert bst_full.root.val == 8

    # Right Nodes
    assert bst_full.root.right.parent.val == 8
    assert bst_full.root.right.right.parent.val == 12
    assert bst_full.root.right.right.right.parent.val == 13
    assert bst_full.root.right.left.parent.val == 12
    assert bst_full.root.right.left.left.parent.val == 11

    # Left Nodes
    assert bst_full.root.left.parent.val == 8
    assert bst_full.root.left.left.parent.val == 4
    assert bst_full.root.left.right.parent.val == 4
    assert bst_full.root.left.left.right.parent.val == 0


def test_search_finds_node(bst_full):
    """Test that search returns node on right."""
    assert bst_full.search(11).val == 11


def test_search_finds_node_left(bst_full):
    """Test that search returns node on left."""
    assert bst_full.search(3).val == 3


def test_search_returns_none(bst_full):
    """Test that search returns None when node not in bst."""
    assert bst_full.search(30) is None


def test_size(bst_full):
    """Test that size is correct."""
    assert bst_full.size() == 10


def test_cotain_true(bst_full):
    """Test that contain returns true if node in bst."""
    assert bst_full.contains(100) is True


def test_cotain_false(bst_full):
    """Test that contain returns false if node not in bst."""
    assert bst_full.contains(99) is False


def test_cotain_false_empty(bst):
    """Test that contain returns true if node in bst."""
    assert bst.contains(99) is False


def test_depth_root_node(bst_full):
    """Test that root node keeps track of depth."""
    assert bst_full.depth() == 3


def test_depth_root_node_small_tree(bst):
    """Test that root node keeps track of depth."""
    bst.insert(8)
    assert bst.depth() == 0
    bst.insert(2)
    assert bst.depth() == 1
    bst.insert(1)
    assert bst.depth() == 2
    assert bst.root.left.depth == 1
    assert bst.root.left.left.depth == 0


def test_depth_root_node_single(bst):
    """Test that root node keeps track of depth."""
    bst.insert(8)
    assert bst.depth() == 0


def test_depth_updates_parent(bst_full):
    """Test that root node keeps track of depth on each node below itself."""
    assert bst_full.root.depth == 3
    # Right Nodes
    assert bst_full.root.right.depth == 2
    assert bst_full.root.right.right.depth == 1
    assert bst_full.root.right.right.right.depth == 0
    assert bst_full.root.right.left.depth == 1
    assert bst_full.root.right.left.left.depth == 0

    # Left Nodes
    assert bst_full.root.left.depth == 2
    assert bst_full.root.left.left.depth == 1
    assert bst_full.root.left.right.depth == 0
    assert bst_full.root.left.left.right.depth == 0


def test_balanced(bst_full):
    """Test the balance of full tree is 0."""
    assert bst_full.balance() == 0


def test_balance_empty(bst):
    """Test the balance of empty tree is error."""
    with pytest.raises(ValueError):
        bst.balance()


def test_balance_left_only(bst):
    """Test balance with only left nodes."""
    bst.insert(8)
    bst.insert(7)
    bst.insert(6)
    bst.insert(5)
    assert bst.balance() == 3


def test_balance_right_only(bst):
    """Test balance with only right nodes."""
    bst.insert(8)
    bst.insert(9)
    bst.insert(10)
    bst.insert(11)
    assert bst.balance() == -3


def test_balance_right_and_one_left(bst):
    """Test balance with one left node."""
    bst.insert(8)
    bst.insert(9)
    bst.insert(10)
    bst.insert(11)
    bst.insert(6)
    assert bst.balance() == -2


def test_bst_iterable_on_init():
    """Test that inits with iterable."""
    from bst import BST
    bst = BST([8, 7, 6, 9, 10, 2, 99])
    assert bst._count == 7


def test_bst_in_order_trav_line_left(bst):
    """Return in order traversal for bst."""
    bst.insert(8)
    bst.insert(7)
    bst.insert(6)
    nodes = []
    gen = bst.in_order()
    for _ in range(bst.size()):
        node = next(gen)
        nodes.append(node)
    assert nodes == [6, 7, 8]


def test_bst_in_order_trav(bst):
    """Return in order traversal for bst."""
    bst.insert(8)
    bst.insert(4)
    bst.insert(6)
    bst.insert(2)
    nodes = []
    gen = bst.in_order()
    for _ in range(bst.size()):
        node = next(gen)
        nodes.append(node)
    assert nodes == [2, 4, 6, 8]


def test_bst_full_in_order_trav(bst_full):
    """Test bst in order trav with full bst."""
    nodes = []
    gen = bst_full.in_order()
    for _ in range(bst_full.size()):
        node = next(gen)
        nodes.append(node)
    assert nodes == [0, 3, 4, 6, 8, 9, 11, 12, 13, 100]


def test_bst_in_order_trav_only_right(bst):
    """Return in order traversal for bst with only right nodes."""
    bst.insert(8)
    bst.insert(10)
    bst.insert(12)
    bst.insert(11)
    nodes = []
    gen = bst.in_order()
    for _ in range(bst.size()):
        node = next(gen)
        nodes.append(node)
    assert nodes == [8, 10, 11, 12]


def test_bst_pre_order_trav(bst):
    """Test pre order trav."""
    bst.insert(8)
    bst.insert(4)
    bst.insert(6)
    bst.insert(2)
    nodes = []
    gen = bst.pre_order()
    for _ in range(bst.size()):
        node = next(gen)
        nodes.append(node)
    assert nodes == [8, 4, 2, 6]


def test_bst_full_pre_order_trav(bst_full):
    """Test bst in pre order trav with full bst."""
    nodes = []
    gen = bst_full.pre_order()
    for _ in range(bst_full.size()):
        node = next(gen)
        nodes.append(node)
    assert nodes == [8, 4, 0, 3, 6, 12, 11, 9, 13, 100]


def test_bst_post_order(bst):
    """Test bst post order."""
    bst.insert(4)
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    nodes = []
    gen = bst.post_order()
    for _ in range(bst.size()):
        node = next(gen)
        nodes.append(node)
    assert nodes == [1, 3, 2, 4]


def test_bst_full_post_order_trav(bst_full):
    """Test bst in post order trav with full bst."""
    nodes = []
    gen = bst_full.post_order()
    for _ in range(bst_full.size()):
        node = next(gen)
        nodes.append(node)
    assert nodes == [3, 0, 6, 4, 9, 11, 100, 13, 12, 8]


def test_bst_full_breadth_first_trav(bst_full):
    """Test for breadth first traversal."""
    nodes = []
    gen = bst_full.breadth_first()
    for _ in range(bst_full.size()):
        node = next(gen)
        nodes.append(node)
    assert nodes == [8, 4, 12, 0, 6, 11, 13, 3, 9, 100]



