# Undirected Graph Implementation in Python
# This module provides a basic undirected graph using an adjacency matrix, with methods to add edges and display

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices  # Number of vertices
        self.graph = [[0] * vertices for i in range(vertices)]  # Adjacency list representation
        self.visited = [False] * vertices  # Track visited vertices for DFS

    def add_edge(self, u, v):
        """Add an edge to the graph."""
        # Graph is undirected
        self.graph[u -1][v - 1] = 1
        self.graph[v -1][u - 1] = 1

    def show_graph(self):
        """Display the adjacency list of the graph."""
        for i in self.graph:
            for j in i:
                print(j, end=' ')
            print("")

    def hasConnection(self, u, v):
        """Check if there is a connection between two vertices."""
        if self.graph[u - 1][v - 1] == 1:
            return True
        return False
    
    def dfs(self, start):
        """Depth First Search to traverse the graph."""
        self.visited[start - 1] = True
        print(f"Visited {start}")
        for i in range(self.vertices):
            if self.graph[start - 1][i] == 1 and not self.visited[i]:
                self.dfs(i + 1)  # Convert to 1-based index for user-friendly output

# Example usage:
g = Graph(5)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)

# This will display the edges in the graph.
g.show_graph() # Output will show the adjacency list representation of the graph.

print(g.hasConnection(1, 3))  # Output: True - 1 has connection with 3
print(g.hasConnection(2, 4))  # Output: False - 2 has no connection with 4

# This will perform a DFS starting from vertex 1.
print(g.dfs(1))