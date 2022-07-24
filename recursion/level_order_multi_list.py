# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        order = []
        children = []
        staging = []
        parents = []
        if root is not None:
            parents.append(root)
        while parents:
            while parents:
                curr = parents[0]
                if curr:
                    staging.append(curr.val)
                if curr and curr.left:
                    children.append(curr.left)
                if curr and curr.right:
                    children.append(curr.right)
                parents.remove(curr)
            order.append(staging)
            parents = children
            children = []
            staging = []
        return order
        