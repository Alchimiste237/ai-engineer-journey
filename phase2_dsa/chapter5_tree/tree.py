class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#        10
#       /  \
#      5    15
#     / \     \
#    3   7     20

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)
