class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        store = {}
        cnt = 0
        for num in nums:
            if num in store:
                cnt += store[num]
                store[num] += 1
            else:
                store[num] = 1
        return cnt