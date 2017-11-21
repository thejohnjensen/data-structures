"""Test module for the binary search tree."""


def test_bst_exists(bst):
    """Test that fixture creates BST."""
    assert bst


def test_bst_root(bst):
    """Test that a root node is created."""
    bst.insert(8)
    assert bst.root.val == 8


def test_bst_three_nodes(bst):
    """Test a bst with root and a node on left and right."""
    bst.insert(8)
    bst.insert(4)
    bst.insert(12)
    assert bst.root.left == 4
    assert bst.root.right == 12