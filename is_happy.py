class Solution:
    def isHappy(self, n: int) -> bool:
        tried = {}
        while n != 1:
            if n in tried:
                return False
            else:
                tried[n] = 1
            n = sum([int(x) ** 2 for x in str(n)])
        return True