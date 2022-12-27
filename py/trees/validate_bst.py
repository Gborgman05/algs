# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        max_int = 2147483648
        def helper(root, low, high):
            if root and root.val < high and root.val > low:
                return helper(root.left, low, root.val) and helper(root.right, root.val, high)
            elif root is None:
                return True
            else:
                return False
        return helper(root, -max_int, max_int)