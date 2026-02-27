# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, l_min, r_max):
            if not node:
                return True
            if node.val >= r_max:
                return False
            if node.val <= l_min:
                return False
            # print(node.val)
            # print(l_min)
            # print(r_max)
            # print()
            return helper(node.left, l_min, min(node.val, r_max)) and helper(node.right, max(node.val, l_min), r_max)
        return helper(root, -float("inf"), float("inf"))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # validate left tree, validate right tree
        def helper(l_min, r_max, root):
            if not root:
                return True
            if root.val > l_min and root.val < r_max:
                return helper(l_min, root.val, root.left) and helper(root.val, r_max, root.right)
            else:
                return False
        if not root:
            return True
        return helper(float('-inf'), root.val, root.left) and helper(root.val, float('inf'), root.right)

        

    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def max_val_is_tree(node):
            if not node:
                return (0, 0, True)
            l_max = l_min = r_max = r_min = node.val
            l_is_tree = r_is_tree = True # empty is a tree
            if node.left:
                l_max, l_min, l_is_tree =  max_val_is_tree(node.left)
            if node.right:
                r_max, r_min, r_is_tree =  max_val_is_tree(node.right)
            my_max = max(l_max, r_max, node.val)
            my_min = min(l_min, r_min, node.val)
            is_tree = True # do this because only compare values if they exist
            if node.left:
                is_tree = is_tree and node.val > l_max and l_is_tree
            if node.right:
                is_tree = is_tree and node.val < r_min and r_is_tree
            return (my_max, my_min, is_tree)
        return max_val_is_tree(root)[2]
