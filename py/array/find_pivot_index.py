# https://leetcode.com/problems/find-pivot-index/submissions/
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        index = 0
        right -= nums[0]
        while index + 1 < len(nums):
            print(left)
            print(right)
            if left == right:
                return index
            left += nums[index]
            right -= nums[index + 1]
            index += 1
        if left == right:
            return index
        else:
            return -1
        