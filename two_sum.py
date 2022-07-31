class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        values = {}
        for i in range(len(nums)):
            if nums[i] * 2 == target and nums[i] in table:
                return [table[nums[i]], i]
            table[nums[i]] = i
            if target - nums[i] in table and table[target - nums[i]] !=  i:
                return [table[target - nums[i]], i]