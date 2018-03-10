"""."""
from collections import defaultdict as dd


class Graph(object):

    def __init__(self):
        self.graph = dd(list)

    def add_node(self, data):
        self.graph[data]

    def add_edge(self, start, end, weight):
        self.graph[start].append((end, weight))
        self.graph[end].append((start, weight))

    def dfs(self, start, end):
        pass

    def bfs():
        pass

    def dykstras(self):
        pass

data = [
    [1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [1, 1, 1, 1, 0]
]

graph = {
    'A': ['B', 'Q'],
    'B': ['C'],
    'C': ['D'],
    'D': ['F'],
    'F': ['G'],
    'H': ['I'],
    'I': ['J'],
    'J': ['K'],
    'K': ['E'],
}


if __name__ == '__main__':
    g = Graph()
    g.add_edge('a', 'b', 2)
    g.add_edge('a', 'c', 3)
    g.add_edge('a', 'd', 1)
    g.add_edge('c', 'b', 1)
    g.add_edge('d', 'c', 5)
