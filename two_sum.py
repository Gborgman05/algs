# O(n) where n is the length of the list
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for index, num in enumerate(nums):
            if target - num in store:
                return [index, store[target - num]]
            else:
                store[num] = index
        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            sm = numbers[l] + numbers[r]
            if sm < target:
                l += 1
            elif sm > target:
                r -= 1
            else:
                return [l+1, r+1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            if target - nums[i] in store:
                return [i, store[target - nums[i]]]
            else:
                store[nums[i]] = i
        return []
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            if target - nums[i] in store:
                return [i, store[target - nums[i]]]
            else:
                store[nums[i]] = i
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_i = {}
        for i in range(len(nums)):
            if target - nums[i] in val_to_i:
                return [i, val_to_i[target - nums[i]]]
            val_to_i[nums[i]] = i

            
        
                