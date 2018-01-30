"""Graph created with seperate classes for Node and Graph."""


class Node(object):
    """Node for graph."""

    def __init__(self, node):
        """."""
        self.node = node
        self.edge = None


class Graph(object):
    """Graph data structure."""

    def __init__(self):
        """."""
        self.graph = {}

    def add_node(self, node):
        """."""
        self.graph[Node(node)]

    def add_edge(self, cur_node, to_node):
        """."""
        pass

