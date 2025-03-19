# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        cnt = 0
        levels = 0
        while True:
            if not root:
                return 0
            if root.left and root.right:
                levels += 1
                root = root.right
            elif root.left:
                return self.calcCount(levels, isRight)
            elif not root.left and not root.right:
                return self.calcCount(levels)
    def calcCount(self, levels, isRight):
        sm = 0
        for i in range(levels + 1):
            sm += 2 ** i

        print(levels)
        return sm