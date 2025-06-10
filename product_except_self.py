class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = {}
        suffixes = {}
        for i in range(len(nums)):
            if i == 0:
                prefixes[0] = 1
            else:
                prefixes[i] = prefixes[i-1] * nums[i-1]
        
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                suffixes[i] = 1
            else:
                suffixes[i] = suffixes[i+1] * nums[i+1]
        return [prefixes[i] * suffixes[i] for i in range(len(nums))]
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                before[i] = before[i-1] * nums[i-1]

        suffix = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i+1] *nums[i+1]
        return [before[i] * suffix[i] for i in range(len(nums))]