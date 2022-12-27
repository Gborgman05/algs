# DP problem based on an array of jumps possible at each step
# minimizing the total jumps

class Solution:
    def jump(self, nums: List[int]) -> int:
        store = [0]
        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                # print("i ", i)
                # print("j ", j)
                if len(store) >= len(nums):
                    return store[len(nums) - 1]
                if len(store) <= i + j:
                    store.append(store[i] + 1)
                else:
                    store[i + j] = min(store[i + j], store[i] + 1)
        return store[len(nums) -1]