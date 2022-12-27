# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        high = 2147483648 + 1
        low = -2147483648 - 1
        def helper(high, low, node):
            if not node:
                return True
            else:
                return node.val < high and node.val > low and helper(node.val, low, node.left) and helper(high, node.val, node.right)
        return helper(high, low, root)
        