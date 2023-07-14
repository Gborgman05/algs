# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root:
            print(targetSum)
            return (targetSum==root.val and not root.left and not root.right) or Solution.hasPathSum(self, root.left, targetSum - root.val) or Solution.hasPathSum(self, root.right, targetSum - root.val)
        return False