# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return -1
            else:
                return 1 + max(height(node.left), height(node.right))
        if not root:
            return True
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right) and 2 > abs(height(root.left) - height(root.right))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node):
            if not node:
                return 0
            else:
                return max(get_height(node.left), get_height(node.right)) + 1
        if not root:
            return True
        return abs(get_height(root.left) - get_height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isBalancedAndHeight(node):
            if not node:
                return (True, 0)
            else:
                l = isBalancedAndHeight(node.left)
                r = isBalancedAndHeight(node.right)
                return (l[0] and r[0] and 1 >=abs(l[1] - r[1]), 1 + max(l[1], r[1]))
        
        return isBalancedAndHeight(root)[0]
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (True, 0)
            else:
                l = dfs(node.left)
                r = dfs(node.right)
                return (l[0] and r[0] and abs(l[1] - r[1]) <= 1, 1 + max(l[1], r[1]))
        return dfs(root)[0]