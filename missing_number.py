class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = (len(nums) * (len(nums)+1)) // 2
        return total - sum(nums)
        # sum of 1, 2, 3, n is n(n+1)/2