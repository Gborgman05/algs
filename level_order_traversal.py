# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        final = []
        curr= [root]
        if not root:
            return []

        while curr:
            lvl = []
            tmp = []
            for node in curr:
                if node:
                    tmp.append(node.val)
                    if node.left:
                        lvl.append(node.left)
                    if node.right:
                        lvl.append(node.right)
            final.append(tmp)
            curr = lvl
        return final
        