# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return 0
            else:
                print(node.val)
                l = helper(node.left)
                r = helper(node.right)
                print("max ", max(node.val, l + node.val, r + node.val, l + r + node.val, l, r))
                return max(node.val, l + node.val, r + node.val, l + r + node.val, l, r)
        return helper(root)