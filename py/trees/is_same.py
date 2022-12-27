# code adapted from is_sym because symmetry very similar to equality
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        n = q
        q = []
        q2 = []
        todo = []
        todo.append(p)
        while todo:
            cur = todo.pop(0)
            if cur:
                q.append(cur.val)
            else:
                q.append(None)
            if cur:
            # if cur.left:
                todo.append(cur.left)
            # if cur.right:
                todo.append(cur.right)
        todo.append(n)
        while todo:
            cur = todo.pop(0)
            if cur:
                q2.append(cur.val)
            else:
                q2.append(None)
            if cur:
                todo.append(cur.left)
                todo.append(cur.right)
        # print(q)
        return q == q2