class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0 if nums[0] == target else -1
        else:
            l = 0
            r = len(nums) - 1
            while l <= r:
                midpoint = ((r - l) // 2) + l
                if nums[midpoint] > target:
                    r = midpoint - 1
                elif nums[midpoint] < target:
                    l = midpoint + 1
                else:
                    return midpoint
            return -1