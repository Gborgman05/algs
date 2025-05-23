class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []
        curr = []
        def helper(l):
            if len(nums) == l:
                final.append(curr[:])
                return
            
            curr.append(nums[l])
            helper(l + 1)

            curr.pop()
            helper(l + 1)

        
        helper(0)
        return final 