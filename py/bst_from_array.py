# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid = len(nums) // 2
        base = TreeNode(nums[mid])
        l_side = base
        r_side = base
        for i in range(mid - 1, -1, -1):
            node = TreeNode(nums[i])
            l_side.left = node
            l_side = l_side.left
        for i in range(mid + 1, len(nums)):
            r_side.right = TreeNode(nums[i])
            r_side = r_side.right
        return base
            