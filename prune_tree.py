# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def contains_one(root):
            # print("here")
            if not root:
                return False
            if root.val == 1:
                return True
            else:
                # print(root)
                # print(contains_one(root.left) or contains_one(root.right))
                return contains_one(root.left) or contains_one(root.right)
        def check_subtree(root):
            # print(root)
            if not root:
                return None
            if not contains_one(root.left):
                # print(root.val)
                root.left = None
            else:
                root.left = check_subtree(root.left)
            if not contains_one(root.right):
                root.right = None
            else:
                root.right = check_subtree(root.right)
            if root.right or root.left or root.val == 1:
                return root
        return check_subtree(root)