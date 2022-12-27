# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def  helper(arr, start, end):
            if start <= end:
                mid = (end - start) // 2 + start
                return TreeNode(nums[mid], helper(arr, start, mid - 1), helper(arr, mid + 1, end))
        return helper(nums, 0, len(nums) - 1)
            
        
            