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
            
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        rob_total = [0] * len(nums)
        rob_total[0] = nums[0]
        rob_total[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)): 
            rob_total[i] = max(rob_total[i-1], rob_total[i-2] + nums[i])
        # print(rob_total)
        return rob_total[-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        max_loot = [0] * len(nums)
        if len(nums) <= 2:
            return max(nums)
        max_loot[0], max_loot[1] = nums[0], max(nums[1], nums[0])
        for i in range(2, len(max_loot)):
            max_loot[i] = max(max_loot[i-2] + nums[i], max_loot[i-1])
        return max_loot[-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        # do it assuming first house is robbed, then do it assuming last house is robbed
        # first house
        if len(nums) < 3:
            return max(nums)
        take = [0] * (len(nums) -1)
        take[0] = nums[0]
        take[1] = nums[0]
        for i in range(2, len(take)):
            take[i] = max(take[i-1], take[i-2] + nums[i])
        
        #last house
        take2 = [0] * (len(nums))
        take2[0] = 0
        take2[1] = take2[0] + nums[1]
        for i in range(2, len(take2)):
            take2[i] = max(take2[i-1], take2[i-2] + nums[i])
        return max (take[-1], take2[-1])


