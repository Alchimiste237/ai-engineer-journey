from collections import defaultdict

class Graph:
    def __init__(self, directed=False):
        self.adjacency_list = defaultdict(list)
        self.directed = directed

    def add_vertex(self, vertex):
        """Add a vertex with no edges."""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, u, v, weight=None):
        """Add edge from u to v (and v to u if undirected)."""
        self.adjacency_list[u].append((v, weight) if weight else v)
        if not self.directed:
            self.adjacency_list[v].append((u, weight) if weight else u)

    def get_neighbors(self, vertex):
        """Return all neighbors of a vertex."""
        return self.adjacency_list[vertex]

    def has_edge(self, u, v):
        """Check if edge exists between u and v."""
        return v in self.adjacency_list[u]

    def vertices(self):
        """Return all vertices."""
        return list(self.adjacency_list.keys())

    def __str__(self):
        result = []
        for vertex, neighbors in self.adjacency_list.items():
            result.append(f"{vertex} → {neighbors}")
        return "\n".join(result)


# Build the example graph
g = Graph()
for edge in [("A","B"), ("A","C"), ("A","D"), ("B","E"), ("D","E")]:
    g.add_edge(*edge)
print(g)
