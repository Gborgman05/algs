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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = -99999999
        def max_gain(node):
            if node is None:
                return 0
            left = max(max_gain(node.left), 0)
            right = max(max_gain(node.right), 0)
            current_max_path = node.val + left + right
            self.max_path = max(self.max_path, current_max_path)
            
            return node.val + max(left, right)
        max_gain(root)
        return self.max_path