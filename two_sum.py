# O(n) where n is the length of the list
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for index, num in enumerate(nums):
            if target - num in store:
                return [index, store[target - num]]
            else:
                store[num] = index
        