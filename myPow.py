class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        while n > 0:
            ans *= x
            n -= 1
        while n < 0:
            ans /= x
            n += 1

        return ans
        # this could be optimized with recursion to find a faster solution