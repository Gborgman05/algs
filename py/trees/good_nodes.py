# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def sub(node, max_val):
            if node:
                if node.val < max_val:
                    return sub(node.left, max_val) + sub(node.right, max_val)
                else:
                    max_val = node.val
                    return 1 + sub(node.left, max_val) + sub(node.right, max_val)
            return 0
        return sub(root, -100001)
