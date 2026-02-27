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
                


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []
        if not root:
            return []
        q = [root]
        while q:
            next_level =[]
            curr = []
            for node in q:
                if node:
                    curr.append(node.val)
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
            levels.append(curr)
            q = next_level
        return [row[-1] for row in levels]


        