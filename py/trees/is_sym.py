# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = []
        q2 = []
        todo = []
        todo.append(root.left)
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
        todo.append(root.right)
        while todo:
            cur = todo.pop(0)
            if cur:
                q2.append(cur.val)
            else:
                q2.append(None)
            if cur:
                # have to flip enqeueing step because mirrored around the center node
            # if cur.right:
                todo.append(cur.right)
            # if cur.left:
                todo.append(cur.left)
        # print(q)
        return q == q2