# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return [""]
        elif not root.left and not root.right:
            return [str(root.val)]
        elif root.left and root.right:
            return [str(root.val) + "->" + i for i in self.binaryTreePaths(root.left)] + [str(root.val) + "->" + i for i in self.binaryTreePaths(root.right)] 
        elif root.right:
            return [str(root.val) + "->" + i for i in self.binaryTreePaths(root.right)] 
        elif root.left:
            return [str(root.val) + "->" + i for i in self.binaryTreePaths(root.left)] 

