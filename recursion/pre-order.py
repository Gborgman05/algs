"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        order = []
        def helper(node):
            order.append(node.val)
            for child in node.children:
                helper(child)
        if root:
            helper(root)
        return order