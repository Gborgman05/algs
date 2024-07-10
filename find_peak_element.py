class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l = 0
        r = len(nums) - 1
        while r > l:
            piv = (r + l) // 2
            if nums[piv] > nums[piv+1] and nums[piv] > nums[piv-1]:
                return piv
            
            if nums[piv] < nums[piv+1]:
                l = piv + 1
            else:
                r = piv - 1
        return l