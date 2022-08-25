class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # l = nums[:(len(nums) - k)]
        # r = nums[len(nums) - k:]
        # nums = l + r
        saved = []
        k = k % len(nums)
        for i in range(k):
            saved.append(nums.pop())
        # does multiple insertions at once
        nums[0:0] = reversed(saved)
            