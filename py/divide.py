class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # weird edge case I don't understand from leetcode
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        neg = (divisor < 0) ^ (dividend < 0)
        if divisor < 0:
            divisor = -divisor
        if dividend < 0:
            dividend = -dividend
        count = 0
        cur_counter = 1
        cur_divisor = divisor
        while dividend >= divisor:
            while dividend >= cur_divisor + cur_divisor:
                cur_divisor = cur_divisor + cur_divisor
                cur_counter = cur_counter + cur_counter
                dividend -= cur_divisor
                count += cur_counter
            cur_divisor = divisor
            cur_counter = 1
            if dividend >= divisor:
                count += 1
                dividend -= divisor


        if neg:
            count = -count
        return count 