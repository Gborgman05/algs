class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        final = []

        def helper(curr, i):
            if i >= len(nums):
                final.append(curr[:])
                return
            curr.append(nums[i])
            # include
            helper(curr, i + 1)
            curr.pop()
            # don't include
            while len(nums) > i + 1 and nums[i+1] == nums[i]:
                i += 1
            helper(curr, i + 1)
        helper([], 0)
        return final