class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 2 == 0:
            n /= 2
        if n == 1 or n == -1:
            return True
        return False