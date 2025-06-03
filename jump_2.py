class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        jumps = [0] + ([float("inf")] * (len(nums)-1))
        for i in range(len(nums)-1):
           for j in range(nums[i]+1):
            #print(i, j)
            if i + j < len(jumps):
                jumps[i+j] = min(jumps[i+j], jumps[i] + 1)
       # print(jumps)
        return jumps[-1]



        