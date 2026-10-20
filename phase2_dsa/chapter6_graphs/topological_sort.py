from collections import deque
from graph import Graph

def topological_sort(graph):
    """
    Kahn's algorithm using BFS + in-degree tracking.
    Only works on DAGs (directed acyclic graphs).
    Returns None if cycle detected.
    """
    # Count incoming edges for each vertex
    in_degree = {v: 0 for v in graph.vertices()}
    for vertex in graph.vertices():
        for neighbor in graph.get_neighbors(vertex):
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1

    # Start with all vertices that have no dependencies
    queue = deque([v for v, deg in in_degree.items() if deg == 0])
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph.get_neighbors(vertex):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(graph.vertices()):
        return None   # cycle detected — topological sort impossible

    return result


# ML pipeline dependencies
pipeline = Graph(directed=True)
tasks = [
    ("load_data", "preprocess"),
    ("preprocess", "feature_engineering"),
    ("feature_engineering", "train"),
    ("train", "evaluate"),
    ("evaluate", "deploy")
]
for u, v in tasks:
    pipeline.add_edge(u, v)

order = topological_sort(pipeline)
print("Execution order:", order)
# ['load_data', 'preprocess', 'feature_engineering', 'train', 'evaluate', 'deploy']
