class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        store = {}
        for num in nums:
            store[num] = 1
        
        for i in range(0, len(nums) + 1):
            if i not in store:
                return i
        