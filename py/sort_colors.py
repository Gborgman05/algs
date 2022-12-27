class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = 0
        i = 0
        while i < len(nums):
            while i < len(nums) and nums[i] == cur:
                i+= 1
            if i < len(nums) and nums[i] > cur:
                # find something to swap
                j = i
                while j < len(nums) and nums[j] != cur:
                    j += 1
                if j >= len(nums):
                    # there is nothing to swap
                    cur += 1
                    continue
                else:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
                    