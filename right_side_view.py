# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [root]
        final = []

        while q:
            final.append(q[-1].val)
            nxt_lvl = []
            for tmp in q:
                if tmp and tmp.left:
                    nxt_lvl.append(tmp.left)
                if tmp and tmp.right:
                    nxt_lvl.append(tmp.right)
            q = nxt_lvl
        return final
                
