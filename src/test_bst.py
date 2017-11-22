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


def test_depth_root_node_single(bst):
    """Test that root node keeps track of depth."""
    bst.insert(8)
    assert bst.depth() == 0


# def test_depth_updates_parent(bst_full):
#     """Test that root node keeps track of depth on each node."""
#     assert bst_full.root.depth == 3
#     # Right Nodes
#     assert bst_full.root.right.depth == 2
#     assert bst_full.root.right.right.depth == 1
#     assert bst_full.root.right.right.right.depth == 0
#     assert bst_full.root.right.left.depth == 1
#     assert bst_full.root.right.left.left.depth == 0

#     # Left Nodes
#     assert bst_full.root.left.depth == 2
#     assert bst_full.root.left.left.depth == 1
#     assert bst_full.root.left.right.depth == 1
#     assert bst_full.root.left.left.right.depth == 0