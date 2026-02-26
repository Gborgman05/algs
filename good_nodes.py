# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, max_val):
            if not node:
                return 0
            add = 0
            if max_val <= node.val:
                max_val = node.val
                add = 1
            return helper(node.left, max_val) + helper(node.right, max_val) + add
        return helper(root, float('-inf'))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def caller(highest_parent, child):
            if not child:
                return 0
            add = 1 if child.val >= highest_parent else 0
            return add + caller(max(child.val, highest_parent), child.left) + caller(max(child.val, highest_parent), child.right)
        if not root:
            return 0
        return caller(root.val, root)
        