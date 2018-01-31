"""Test for graph_b data structure."""


def test_create_graph(graph_b):
    """."""
    assert graph_b.graph == {}


def test_graph_one_node(graph_b):
    """."""
    graph_b.add_node('A')
    assert graph_b.graph == {'A': set()}


def test_add_edge(graph_b):
    """."""
    graph_b.add_node('A')
    graph_b.add_node('B')
    nodes = []
    for node in graph_b.graph.keys():
        nodes.append(node)
    assert 'A' and 'B' in nodes
#     graph_b.add_edge('A', 'B')
#     assert graph_b.graph[0].nodes[0].data == 'B'


# def test_add_edge_to_non_existing_node(graph_b):
#     """."""
#     graph_b.add_node('A')
#     graph_b.add_node('B')
#     graph_b.add_edge('A', 'B')
#     graph_b.add_edge('A', 'E')
#     assert graph_b.graph[2].data == 'E'
#     assert graph_b.graph[0].nodes[0].data == 'B'
#     assert graph_b.graph[0].nodes[1].data == 'E'