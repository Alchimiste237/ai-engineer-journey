# ── Depth-First Search (DFS) ───────────────────────────────────────

def inorder(node):
    """Left → Root → Right. Gives SORTED output for a BST."""
    if node is None:
        return []
    return inorder(node.left) + [node.data] + inorder(node.right)

def preorder(node):
    """Root → Left → Right. Used to COPY or SERIALIZE a tree."""
    if node is None:
        return []
    return [node.data] + preorder(node.left) + preorder(node.right)

def postorder(node):
    """Left → Right → Root. Used to DELETE a tree or evaluate expressions."""
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.data]

# ── Breadth-First Search (BFS) ─────────────────────────────────────

from collections import deque

def level_order(root):
    """
    Level by level, left to right.
    Used to find shortest path, print tree level by level.
    Requires a queue (not recursion).
    """
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.data)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result
