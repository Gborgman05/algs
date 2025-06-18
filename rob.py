class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        money = [0] * len(nums)
        money[0] = nums[0]
        money[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            money[i] = max(money[i-1], nums[i] + money[i-2])
        return money[-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        money = [0] * len(nums)
        money[0] = nums[0]
        money[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            money[i] = max(money[i-1], money[i-2] + nums[i])
        #print(money)
        return money[-1]
            
        