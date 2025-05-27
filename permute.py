class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final = []
        def helper(curr, rem):
            if len(curr) == len(nums):
                final.append(curr[:])
                return
            for i in range(len(rem)):
                curr.append(rem[i])
                helper(curr, rem[:i] + rem[i+1:])
                curr.pop()
        helper([], nums)
        return final