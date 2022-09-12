class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        pos = True
        if dividend < 0 and divisor < 0:
            pass
        elif dividend > 0 and divisor > 0:
            pass
        else:
            pos = False
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        while dividend >= divisor:
            dividend -= divisor
            count += 1
        if not pos:
            count = -count
        return count