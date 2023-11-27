from graph import Node, WeightedNode, WeightedGraph

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

print(weighted_graph.dijkstra_shortest_path(weighted_graph.nodes[0], weighted_graph.nodes[2]))