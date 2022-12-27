# optimized for log(n)
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r:
            pivot = l + (r-l) // 2
            calc = pivot * pivot
            calc2 = (pivot+1) * (pivot+1)
            if calc <= x and calc2 > x:
                return pivot
            elif calc > x:
                r = pivot - 1
            else:
                l = pivot + 1
            