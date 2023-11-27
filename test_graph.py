import pytest
from graph import Node, Graph, WeightedNode, WeightedGraph

@pytest.fixture
def sample_graph():
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")

    a.add_child(b, 1)
    a.add_child(c, 1)
    b.add_child(e, 1)
    c.add_child(d, 1)
    d.add_child(e, 1)

    graph = Graph()
    graph.add_node(a)
    graph.add_node(b)
    graph.add_node(c)
    graph.add_node(d)
    graph.add_node(e)

    return graph

def test_dfs(sample_graph):
    graph = sample_graph
    result = graph.dfs(graph.nodes[0])
    assert result == ["A", "B", "E", "C", "D"]

def test_bfs(sample_graph):
    graph = sample_graph
    result = graph.bfs(graph.nodes[0])
    assert result == ["A", "B", "C", "E", "D"]

def test_to_string(sample_graph):
    graph = sample_graph
    result = graph.graph_to_string()
    assert result == "A: B, C\nB: E\nC: D\nD: E\nE: \n"

@pytest.fixture
def weighted_graph():
    a = WeightedNode("A")
    b = WeightedNode("B")
    c = WeightedNode("C")
    d = WeightedNode("D")
    e = WeightedNode("E")

    weighted_graph = WeightedGraph()
    weighted_graph.add_node(a)
    weighted_graph.add_node(b)
    weighted_graph.add_node(c)
    weighted_graph.add_node(d)
    weighted_graph.add_node(e)

    a.add_child(b, 2)
    a.add_child(c, 3)
    b.add_child(e, 5)
    c.add_child(d, 1)
    d.add_child(e, 1)

    return weighted_graph

def test_weighted_graph(weighted_graph):
    assert weighted_graph.get_size() == 5

def test_weighted_bfs(weighted_graph):
    assert weighted_graph.bfs(weighted_graph.nodes[0]) == "Weighted Graph : " + str(["A", "B", "C", "E", "D"])

def test_dijkstra_shortest_path(weighted_graph):
    result = weighted_graph.dijkstra_shortest_path(weighted_graph.nodes[0], weighted_graph.nodes[4])
    assert result == 5

def test_graph_to_string(weighted_graph):
    result = weighted_graph.graph_to_string()
    expected_result = "A -> ['B', 'C']\nB -> ['E']\nC -> ['D']\nD -> ['E']\nE -> []"
    assert result == expected_result


@pytest.fixture
def weighted_graph_2():
    a = WeightedNode("A")
    b = WeightedNode("B")
    c = WeightedNode("C")

    weighted_graph = WeightedGraph()
    weighted_graph.add_node(a)
    weighted_graph.add_node(b)
    weighted_graph.add_node(c)

    a.add_child(b, 1)
    b.add_child(c, 1)
    a.add_child(c, 3)

    return weighted_graph

def test_dijkstra_shortest_path(weighted_graph_2):
    result = weighted_graph_2.dijkstra_shortest_path(weighted_graph_2.nodes[0], weighted_graph_2.nodes[2])
    assert result == 2