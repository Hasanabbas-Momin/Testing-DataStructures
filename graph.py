from queue import Queue
from heapq import heappush, heappop

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def __str__(self):
        return self.data

    def add_child(self, child_node, weight):
        self.children.append((child_node, 0))

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        if isinstance(node, Node):
            self.nodes.append(node)

    def get_size(self):
        return len(self.nodes)

    def dfs(self, start_node, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_node)
        result = [start_node.data]

        for child in start_node.children:
            if child[0] not in visited:
                result.extend(self.dfs(child[0], visited))
        return result

    def bfs(self, start_node):
        visited = set()
        result = []
        queue = Queue()

        queue.put(start_node)
        visited.add(start_node)

        while not queue.empty():
            current_node = queue.get()
            result.append(current_node.data)

            for child in current_node.children:
                if child[0] not in visited:
                    queue.put(child[0])
                    visited.add(child[0])
        self.bfs_res = result
        return result
    def graph_to_string(self):
        result = ""
        for node in self.nodes:
            children = [child[0] for child in node.children]
            result += f"{node.data}: {', '.join(map(str, children))}\n"
        return result

class WeightedNode(Node):
    
    def add_child(self, child_node, weight):
        self.children.append((child_node, weight))

class WeightedGraph(Graph):

    def add_node(self, child_node):
        if isinstance(child_node, WeightedNode):
            self.nodes.append(child_node)

    def dijkstra_shortest_path(self, start_node, end_node):
        distances = {node: float('inf') for node in self.nodes}
        distances[start_node] = 0

        priority_queue = [(0, start_node)]

        while priority_queue:
            current_distance, current_node = heappop(priority_queue)

            if current_node == end_node:
                return distances[end_node]

            for neighbor in current_node.children:
                distance = current_distance + neighbor[1]

                if distance < distances[neighbor[0]]:
                    distances[neighbor[0]] = distance
                    heappush(priority_queue, (distance, neighbor[0]))

    def bfs(self, nod):
        super().bfs(nod)
        return "Weighted Graph : " + str(self.bfs_res)

    def graph_to_string(self):
        result = []
        for node in self.nodes:
            children = [child[0].data for child in node.children]
            result.append(f"{node.data} -> {children}")
        return '\n'.join(result)
    

