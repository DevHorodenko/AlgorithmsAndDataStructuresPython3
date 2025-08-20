class Graph:

    def __init__(self, vertices):
        self.vertices = vertices  # Number of vertices
        self.graph = [[] * vertices for i in range(vertices)]

    def add_edge(self, u, v):
        """Add an edge to the graph."""
        # Graph is directed
        self.graph[u - 1].append(v - 1)

    def show_graph(self):
        """Display the adjacency list of the graph."""
        for i in range(self.vertices):
            print('%d: ' % (i + 1), end='')
            for j in self.graph[i]:
                print('%d -> ' % (j + 1), end=' ')
            print("")

    def hasConnection(self, u, v):
        """Check if there is a connection between two vertices."""
        if v - 1 in self.graph[u - 1]:
            return True
        return False
    
# Example usage:
g = Graph(5)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 5)
g.add_edge(4, 1)
g.add_edge(5, 3)

g.show_graph()  # Output will show the adjacency list representation of the graph.

print(g.hasConnection(1, 2))  # Output: True - 1 has connection with 2
print(g.hasConnection(3, 4))  # Output: False - 3 has no connection with 4