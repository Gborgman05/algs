# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(a, b):
            if not a and not b:
                return True
            elif a and b:
                return a.val == b.val and is_same(a.left, b.left) and is_same(a.right, b.right)
            return False
        
        if not root and not subRoot:
            return True
        elif not root and subRoot:
            return False
        else:
            if root.val == subRoot.val:
                return is_same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



        