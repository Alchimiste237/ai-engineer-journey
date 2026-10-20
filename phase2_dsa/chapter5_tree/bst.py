from tree import TreeNode
from traversal import inorder

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert maintaining BST property. O(log n) average."""
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return TreeNode(data)    # found the right empty spot
        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)
        # if equal, do nothing (no duplicates)
        return node

    def search(self, data):
        """Search for a value. O(log n) average."""
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)

    def delete(self, data):
        """Delete a node. O(log n) average."""
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return None

        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            # Found the node to delete — 3 cases:
            if node.left is None:        # case 1: no left child
                return node.right
            elif node.right is None:     # case 2: no right child
                return node.left
            else:                        # case 3: two children
                # Replace with inorder successor (smallest in right subtree)
                successor = self._find_min(node.right)
                node.data = successor.data
                node.right = self._delete(node.right, successor.data)
        return node

    def _find_min(self, node):
        """Find leftmost node (minimum) in a subtree."""
        while node.left is not None:
            node = node.left
        return node

    def inorder(self):
        """Returns sorted list of all values."""
        return inorder(self.root)

    def __str__(self):
        return f"BST(inorder={self.inorder()})"


# Usage
bst = BST()
for val in [10, 5, 15, 3, 7, 20]:
    bst.insert(val)

print(bst)                  # BST(inorder=[3, 5, 7, 10, 15, 20])
print(bst.search(7))        # True
print(bst.search(99))       # False
bst.delete(5)
print(bst.inorder())        # [3, 7, 10, 15, 20]
