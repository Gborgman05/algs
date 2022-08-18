# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def subrout(root) -> int:
            if not root:
                return 0
            l = subrout(root.left)
            r = subrout(root.right)
            # if either subtree is unbalanced, the tree is unbalanced
            if l is False or r is False:
                # print(root.val)
                # print("gets here")
                return False
            elif l - 1 == r or r - 1 == l or l == r:
                return max(l, r) + 1
            # subtrees are balanced, but their height differs by more than one
            else:
                print(root.val)
                return False
            # weird bool logic at end bc i used multiple return types
        return not (subrout(root) is False)
                