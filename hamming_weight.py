class Solution:
    def hammingWeight(self, n: int) -> int:
        s = 1
        w = 0
        while n:
            if n // 2 == n / 2:
                pass
            else:
                w += 1
            n = n // 2
        return w
                
        