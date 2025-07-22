# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, max_val):
            if not node:
                return 0
            add = 0
            if max_val <= node.val:
                max_val = node.val
                add = 1
            return helper(node.left, max_val) + helper(node.right, max_val) + add
        return helper(root, float('-inf'))