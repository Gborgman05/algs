class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        found = {}
        for num in nums:
            found[num] = 1
        final = []
        for i in range(1, len(nums)+1):
            if i not in found:
                final.append(i)
        return final