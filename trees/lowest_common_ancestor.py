# LOW is defined as closest to root, kinda confusing.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ lowest common ancestor is greater"""
        high = max([p.val, q.val])
        low = min([p.val, q.val])
        node = root
        while True:
            if node.val < low:
                node = node.right
            elif node.val > high:
                node = node.left
            else:
                return node
                
        