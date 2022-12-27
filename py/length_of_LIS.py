class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # O(n^2)
        store = {}
        for i in range(len(nums)):
            # first will be len of subsequence 
            # second will be max value
            if i == 0:
                store[0] = (1, nums[i])
            else:
                poss = 0
                for j in range(i):
                    if nums[j] < nums[i]:
                        poss = max(poss, store[j][0])
                store[i] = (poss + 1, nums[i])
        return max([val[0] for val in store.values()])
