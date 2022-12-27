class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        msum = sum(nums)
        tot = []
        for i in range(len(nums)):
            if i == 0:
                tot.append(1)
            else:
                tot.append(tot[-1] * nums[i-1])
        running = 1
        for i in range(len(nums) - 2, -1, -1):
            running *= nums[i+1]
            tot[i] *= running
        return tot
        