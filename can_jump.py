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

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        max_jump_from_here = nums[0]
        for i in range(len(nums)-1):
            #print(max_jump_from_here)
            
            if max_jump_from_here <= 0:
                return False
            max_jump_from_here = max(max_jump_from_here - 1, nums[i])
        return max_jump_from_here > 0

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 1
        if len(nums) == 1:
            return True
        for num in nums:
            max_jump -= 1
            if max_jump < 0:
                return False
            max_jump = max(max_jump, num)

        return True

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        curr_index = 0
        while curr_index < len(nums) - 1:
            max_jump = max(max_jump-1, nums[curr_index])
            if max_jump < 1:
                return False
            curr_index += 1
        
        return True