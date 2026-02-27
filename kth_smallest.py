# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(node):
            if node:
                return 1 + helper(node.left) + helper(node.right)
            else:
                return 0
        if root:
            tmp = helper(root.left)
            if tmp + 1 == k:
                return root.val
            elif tmp >= k:
                return self.kthSmallest(root.left, k)
            elif tmp < k:
                return self.kthSmallest(root.right, k - tmp - 1)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def count(node):
            if not node:
                return 0
            else:
                return 1 + count(node.left) + count(node.right)
        
        l = count(root.left)
        if k <= l:
            return self.kthSmallest(root.left, k)
        elif k == l + 1:
            return root.val
        elif k > l:
            return self.kthSmallest(root.right, k - l - 1)
            