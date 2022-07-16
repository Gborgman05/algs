class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # srt = sorted(nums)
        final = {}
        i = 0 
        while i < len(nums):
            final[nums[i]] = 1
            i += 1
        mssing = []
        for i in range(1, len(nums) + 1):
            if i not in final:
                mssing.append(i)
        return mssing
