# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            # is there a more concise way to check these nulls?
            if p.left is None and q.left is not None or p.right is None and q.right is not None or q.left is None and p.left is not None or q.right is None and p.right is not None:
                return False
            else:
                return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            # means one is empty
            return p == q
        