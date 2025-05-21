# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # max path is either in the left child, right child or through 
        def max_path(node):
            if not node:
                return (-float("inf"), 0)

            l_max, l_height = max_path(node.left)
            r_max, r_height = max_path(node.right)
            height = node.val + max(l_height, r_height, 0)
            mid_max = node.val + max(0, l_height) + max(0, r_height)
            mid_only = node.val

            return (max(l_max, r_max, height, mid_max, mid_only), height)
        return max_path(root)[0]
        