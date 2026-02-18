class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        final = [0] * (2 * n)
        for i in range(n):
            first = nums[i]
            second = nums[n +i]
            final[2*i] = first
            final[2*i+1] = second
        return final