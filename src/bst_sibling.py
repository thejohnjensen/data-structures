from bst import BST

bst = BST([8, 3, 12, 2, 4, 10, 14, 1, 5, 13])


def assign_sibling(bst):
    visited = [bst.root]
    while visited:
        depth = []
        for node in visited:
            if node.left:
                depth.append(node.left)
            if node.right:
                depth.append(node.right)
        if len(visited) > 1:
            for index, node in enumerate(visited[:-1]):
                node.sibling = visited[index + 1]
        visited = depth

        # now do it with O(1) space complexity