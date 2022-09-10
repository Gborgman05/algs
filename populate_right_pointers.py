"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        saved = root
        levels = []
        l = [root]
        n = []
        while l:
            n = []
            for node in l:
                if node:
                    if node.left:
                        n.append(node.left)
                    if node.right:
                        n.append(node.right)
            levels.append(l)
            l = n
        for level in levels:
            for i in range(len(level)):
                if level[i] == None:
                    continue
                if i < len(level) - 1:
                    level[i].next = level[i+1]
                else:
                    level[i].next = None
        return root
                