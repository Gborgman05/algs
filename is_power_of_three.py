class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        po = 0
        tst = 0
        while n > tst:
            tst = 3 ** po
            if n == tst:
                return True
            po += 1
        return False
                