# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node) -> (int, int):
            # returns (max_length, internally, then max height)
            if not node:
                return (-1, -1)
            max_len, max_height = helper(node.left)
            max_len2, max_height2 = helper(node.right)
            return (max(max_len, max_len2, max_height + max_height2 + 2), max(max_height, max_height2)+ 1)
        if not root:
            return 0
        else:
            return max(helper(root))
        

        