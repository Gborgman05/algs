# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def len_subtree(root):
            if root is None:
                return -1
            else:
                # print("node", root.val, " ", max(len_subtree(root.left), len_subtree(root.right)) + 1)
                return max(len_subtree(root.left), len_subtree(root.right)) + 1
        if root is None:
            return 0
        if root:
            # either completely in left subtree, 
            # entirely in right subtree
            # crosses through root
            l = self.diameterOfBinaryTree(root.left)
            r = self.diameterOfBinaryTree(root.right)
            middle_pass = len_subtree(root.left) + len_subtree(root.right) + 2
            # print(l)
            # print(r)
            # print(middle_pass)
            return max([l, r, middle_pass])
            
            
        