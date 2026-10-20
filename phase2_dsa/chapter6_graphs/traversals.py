from collections import deque

def dfs(graph, start, visited=None):
    """
    Recursive DFS. Explores as far as possible before backtracking.
    Think: maze solving — keep going until you hit a dead end, then backtrack.
    """
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbor in graph.get_neighbors(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

def dfs_iterative(graph, start):
    """
    Iterative DFS using a stack.
    Useful when recursion depth limit is a concern (deep graphs).
    """
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")
            for neighbor in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited

def bfs(graph, start):
    """
    BFS using a queue. Explores all neighbors before going deeper.
    Think: ripple effect — explores in rings outward from start.
    Guarantees shortest path in UNWEIGHTED graphs.
    """
    visited = set([start])
    queue = deque([start])
    order = []

    while queue:
        vertex = queue.popleft()
        order.append(vertex)

        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order
