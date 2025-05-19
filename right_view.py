# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        final = []
        if not root:
            return []
        curr = [root]
        while curr:
            tmp = None
            next_lvl = []
            for node in curr:
                if node:
                    tmp = node.val
                    if node.left:
                        next_lvl.append(node.left)
                    if node.right:
                        next_lvl.append(node.right)
            curr = next_lvl
            if tmp is not None:
                final.append(tmp)
        return final
