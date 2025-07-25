class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = 0
        for a in nums:
            num = num ^ a
        return num