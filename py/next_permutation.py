class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last = nums[0]
        if len(nums) < 2:
            return nums
        for i in range(len(nums)):
            if nums[i] >= last:
                last = nums[i]
            else:
                return nums.sort()
        ptr1 = ptr2 = len(nums) - 1
        while True:
            if ptr1 < 0:
                return nums
            if nums[ptr1] == nums[ptr2]:
                ptr1 -= 1
            else:
                saved = nums[ptr1]
                nums[ptr1] = nums[ptr2]
                nums[ptr2] = saved
                return nums
            