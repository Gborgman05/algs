# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            diameter = max(diameter, left + right)  # update diameter
            return 1 + max(left, right)  # return height

        dfs(root)
        return diameter

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxHeight(self, root):
        if root:
            return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))
        else:
            return 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root:
            if root.left and root.right:
                l, r = self.maxHeight(root.left), self.maxHeight(root.right)
                return max(l + r, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
            if root.right:
                return max(self.maxHeight(root.right), self.diameterOfBinaryTree(root.right))
            if root.left:
                return max(self.maxHeight(root.left), self.diameterOfBinaryTree(root.left))
        return 0
        