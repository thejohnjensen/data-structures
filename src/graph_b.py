"""Graph created with seperate classes for Node and Graph."""
from collections import defaultdict


class Graph(object):
    """Undirected Graph data structure."""

    def __init__(self):
        """Init with defualt dict type set."""
        self.graph = defaultdict(set)

    def add_node(self, data):
        """Add the node to the graph and create set."""
        self.graph[data]

    def add_edge(self, node_a, node_b):
        """Add edge, if end node not in graph add it."""
        self.graph[node_a].add(node_b)
        self.graph[node_b].add(node_a)
    
    def depth_first_search(self):
        """."""
        pass

    def breadth_first_search(self):
        """."""
        pass

    def dykstras(self):
        """."""
        pass

    def bellman_ford(self):
        """."""









