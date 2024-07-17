class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach = [False for num in nums]
        can_reach[0] = True
        for i in range(len(nums)):
            if can_reach[i]:
                j = 1
                while j <= nums[i] and i + j < len(nums):
                    can_reach[i + j] = True
                    j += 1
            if can_reach[-1]:
                return True
        if can_reach[-1]:
            return True
        else:
            return False