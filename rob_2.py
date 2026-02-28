class Solution:
    def rob(self, nums: List[int]) -> int:
        # do it two times
        if len(nums) < 3:
            return max(nums)

        start = [0] * len(nums) 
        start[1] = nums[1]
        for i in range(2, len(nums)):
            start[i] = max(nums[i] + start[i-2], start[i-1])
        op1 = start[-1]
        start = [0] * (len(nums) - 1)
        start[0] = nums[0]
        start[1] = max(nums[1], nums[0])

        for i in range(2, len(nums) - 1):
            start[i] = max(nums[i] + start[i-2], start[i-1])
        op2 = start[-1]
        #print(start)
        return max(op1, op2)
            

class Solution:
    def rob(self, nums: List[int]) -> int:
        # do it assuming first house is robbed, then do it assuming last house is robbed
        # first house
        # actually slightly more nuanced, there is the OPTION to rob the first house in the first pass
        # there is the OPTION to rob the second house
        # otherwise i think you leave open the possibility that neither are hit
        if len(nums) < 3:
            return max(nums)
        max_take = [0] * (len(nums) - 1)
        max_take[0], max_take[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(max_take)):
            max_take[i] = max(max_take[i-2] + nums[i], max_take[i-1])
        top = max_take[-1] 
        max_take = [0] * len(nums)
        max_take[0], max_take[1] = 0, nums[1]
        for i in range(2, len(max_take)):
            max_take[i] = max(max_take[i-2] + nums[i], max_take[i-1])
        return max(top, max_take[-1])

