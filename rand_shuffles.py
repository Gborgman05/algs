import random
class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums

    def reset(self) -> List[int]:
        return self.arr
        

    def shuffle(self) -> List[int]:
        # new = []
        # done = {}
        # while len(new) < len(self.arr):
        #     cur = random.randint(0, len(self.arr))
        #     if cur not in done:
        #         new.append(cur)
        #         done[cur] = 0
        # return new
        cpy = self.arr[:]
        for i in range(len(cpy)):
            swap_idx = random.randrange(i, len(cpy))
            cpy[i], cpy[swap_idx] = cpy[swap_idx], cpy[i]
        return cpy


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()