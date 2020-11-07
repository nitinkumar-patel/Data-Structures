"""
# Edge List
graph = [[0, 2], [2, 3], [2, 1], [1, 3]]

# Adjacent List
graph = [[2], [2, 3], [0, 1, 3], [1, 2]]

# Adjacent Matrix
graph = [
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0],
]


# Adjacent Matrix
graph = {
    0: [0, 0, 1, 0],
    1: [0, 0, 1, 1],
    2: [1, 1, 0, 1],
    3: [0, 1, 1, 0],
}

"""

class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def add_node(self, node):
        self.adjacent_list[node] = []
        self.number_of_nodes += 1

    def add_edge(self, node1, node2):
        # undirected graph
        if node2 not in self.adjacent_list[node1]:
            self.adjacent_list[node1].append(node2)
        if node1 not in self.adjacent_list[node2]:
            self.adjacent_list[node2].append(node1)

    def show_connection(self):
        for node, node_connection in self.adjacent_list.items():
            node_connection = self.adjacent_list[node]
            print(f"{node} --> { ' '.join([i for i in node_connection])}")


if __name__=='__main__':
    my_graph = Graph()
    my_graph.add_node('0')
    my_graph.add_node('1')
    my_graph.add_node('2')
    my_graph.add_node('3')
    my_graph.add_node('4')
    my_graph.add_node('5')
    my_graph.add_node('6')
    my_graph.add_edge('0', '1')
    my_graph.add_edge('0', '2')
    my_graph.add_edge('1', '3')
    my_graph.add_edge('1', '2')
    my_graph.add_edge('2', '4')
    my_graph.add_edge('3', '4')
    my_graph.add_edge('4', '5')
    my_graph.add_edge('5', '6')

    my_graph.show_connection()