class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        num_zeros = 0
        while i < len(nums):
            if nums[i] == 0 and i < len(nums):
                nums.pop(i)
                num_zeros += 1
            else:
                i += 1
        # nums = nums + [0 for i in range(num_zeros)]
        for i in range(num_zeros):
            nums.append(0)
        return nums

        
        