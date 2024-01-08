# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root:
            l = self.diameterOfBinaryTree(root.left)
            r = self.diameterOfBinaryTree(root.right)
            m = self.heightOfTree(root.left) + self.heightOfTree(root.right) 
            # if root.left:
            #     m += 1
            # if root.right:
            #     m += 1
            return max([l, r, m])
        else:
            return 0 
    def heightOfTree(self, root: Optional[TreeNode]) -> int:
        if root:
            return 1 + max(self.heightOfTree(root.left), self.heightOfTree(root.right))            
        else:
            return 0
        
