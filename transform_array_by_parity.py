class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        even = 0
        for num in nums:
            if num % 2 == 0:
                even += 1
        for i in range(len(nums)):
            if i < even:
                nums[i] = 0
            else:
                nums[i] = 1
        return nums 