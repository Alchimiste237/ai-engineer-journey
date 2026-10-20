import heapq

def dijkstra(graph_weighted, start):
    """
    Find shortest distance from start to all other nodes.
    Uses a min-heap (priority queue) to always process cheapest node next.
    O((V + E) log V)

    graph_weighted: dict of {node: [(neighbor, weight), ...]}
    """
    distances = {node: float('inf') for node in graph_weighted}
    distances[start] = 0
    previous = {node: None for node in graph_weighted}

    # min-heap: (distance, node)
    heap = [(0, start)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        # Skip if we already found a better path
        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph_weighted[current_node]:
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(heap, (distance, neighbor))

    return distances, previous

def reconstruct_path(previous, start, end):
    """Reconstruct shortest path from previous node map."""
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    return path if path[0] == start else []


# Example: weighted road network
road_network = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("D", 3), ("E", 1)],
    "C": [("A", 2), ("B", 1), ("D", 5)],
    "D": [("B", 3), ("C", 5), ("E", 2)],
    "E": [("B", 1), ("D", 2)]
}

distances, previous = dijkstra(road_network, "A")
print(distances)
# {'A': 0, 'B': 3, 'C': 2, 'D': 6, 'E': 4}

path = reconstruct_path(previous, "A", "D")
print(f"Shortest path A→D: {path}")
# Shortest path A→D: ['A', 'C', 'B', 'E', 'D']
