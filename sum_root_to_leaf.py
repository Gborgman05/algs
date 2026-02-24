# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def helper(node) -> List[str]:
            if not node:
                return [""]
            else:
                if node.left and node.right:
                    return [str(node.val) + child for child in (helper(node.left) + helper(node.right))]
                if node.right:
                    return [str(node.val) + child for child in helper(node.right)]
                if node.left:
                    return [str(node.val) + child for child in helper(node.left)]
                return [str(node.val)]
        # print(helper(root))
        return sum([int(val, 2) for val in helper(root)])