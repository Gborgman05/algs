class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        store = {0: 1}
        for num in nums:
            new_store = {}
            for key in store:
                if key + num in new_store:
                    new_store[key + num] += store[key]
                else:
                    new_store[key + num] = store[key]
                if key - num in new_store:
                    new_store[key - num] += store[key]
                else:
                    new_store[key - num] = store[key]
            store = new_store
        # print(store)
        if target not in store:
            return 0
        return store[target]