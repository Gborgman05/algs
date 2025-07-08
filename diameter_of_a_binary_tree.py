# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            # returns (longest internal path, longest path ending in the top)
            if not node:
                return (0, 0)
            else:
                l, l_middle = helper(node.left)
                r, r_middle = helper(node.right)
                return (max(l, r, l_middle + r_middle + 1), max(l_middle, r_middle) + 1)


        return max(helper(root)) - 1
        