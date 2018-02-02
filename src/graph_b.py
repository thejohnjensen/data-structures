"""Graph created with seperate classes for Node and Graph."""
from collections import defaultdict
import queue


class Graph(object):
    """Directed Graph data structure."""

    def __init__(self):
        """Init with defualt dict type set."""
        self.graph = defaultdict(list)

    def add_node(self, data):
        """Add the node to the graph and create set."""
        self.graph[data]

    def add_edge(self, start_node, end_node):
        """Add edge, if end node not in graph add it."""
        self.graph[start_node].append(end_node)

    def dfs_recur_1(self, start, visited=[]):
        """."""
        visited += [start]

        for i in self.graph[start]:
            if i not in visited:
                self.dfs_recur_1(i, visited)

        return visited

    def breadth_first_search(self, start):
        """."""
        que = queue.Queue()
        visited = [start]
        que.put(start)
        while not que.empty():
            node = que.get()
            for i in self.graph[node]:
                if i not in visited:
                    visited.append(i)
                    que.put(i)
        return visited

    def dykstras(self):
        """."""
        pass

    def bellman_ford(self):
        """."""


if __name__ == '__main__':
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')
    g.add_edge('D', 'C')
    g.add_edge('E', 'F')
    g.add_edge('F', 'C')





