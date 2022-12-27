# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        order = []
        q = []
        q.append(root)
        while q:
            curr = q[0]
            order.append(curr.val)
            if curr and curr.left:
                q.append(curr.left)
            if curr and curr.right:
                q.append(curr.right)
            q.remove(curr)
        return order
        