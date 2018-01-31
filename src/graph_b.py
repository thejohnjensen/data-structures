"""Graph created with seperate classes for Node and Graph."""


class Node(object):
    """Node for graph."""

    def __init__(self, data):
        """."""
        self.data = data
        self.nodes = []

    def add_edge(self, end):
        """."""
        self.nodes.append(end)


class Graph(object):
    """Graph data structure."""

    def __init__(self):
        """."""
        self.graph = []

    def add_node(self, data):
        """."""
        self.graph.append(Node(data))

    def add_edge(self, start, end):
        """Add edge, if end node not in graph add it."""
        end_node = ''
        found = False
        for node in self.graph:
            if node.data == end:
                end_node = node
                found = True

        if not found:
            end_node = Node(end)
            self.graph.append(end_node)

        for node in self.graph:
            if node.data == start:
                node.add_edge(end_node)
                break







