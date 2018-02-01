"""Graph created with seperate classes for Node and Graph."""
from collections import defaultdict
import Queue


class Graph(object):
    """Directed Graph data structure."""

    def __init__(self):
        """Init with defualt dict type set."""
        self.graph = defaultdict(set)

    def add_node(self, data):
        """Add the node to the graph and create set."""
        self.graph[data]

    def add_edge(self, start_node, end_node):
        """Add edge, if end node not in graph add it."""
        self.graph[start_node].add(end_node)

    def depth_first_search(self):
        """."""
        pass

    def breadth_first_search(self, start):
        """."""
        que = Queue.Queue()
        visited = []
        que.put(start)
        while not que.empty():
            node = que.get()
            visited.append(node)
            for i in self.graph[node]:
                if i not in visited:
                    que.put(i)
        return visited

    def dykstras(self):
        """."""
        pass

    def bellman_ford(self):
        """."""









