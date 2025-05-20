# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, l_min, r_max):
            if not node:
                return True
            if node.val >= r_max:
                return False
            if node.val <= l_min:
                return False
            # print(node.val)
            # print(l_min)
            # print(r_max)
            # print()
            return helper(node.left, l_min, min(node.val, r_max)) and helper(node.right, max(node.val, l_min), r_max)
        return helper(root, -float("inf"), float("inf"))