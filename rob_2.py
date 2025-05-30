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
            
