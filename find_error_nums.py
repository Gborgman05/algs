class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = {}
        duplicated = None
        missed = None
        for num in nums:
            if num in s:
                duplicated = num
            s[num] = 1
        for i in range(1, len(nums)+1):
            if i not in s:
                missed = i
        return [duplicated, missed]

        