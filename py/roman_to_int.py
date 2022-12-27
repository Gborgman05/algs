class Solution:
    def romanToInt(self, s: str) -> int:
        chars = {
            "I":             1,
            "V":             5,
            "X":             10,
            "L":             50,
            "C":             100,
            "D":             500,
            "M":             1000
        }
        print(chars["D"])
        my_sum = 0
        for i in range(len(s)):
            if i > 0 and chars[s[i]] > chars[s[i-1]]:
                my_sum += chars[s[i]]
                my_sum -= 2*chars[s[i-1]]
            else:
                my_sum += chars[s[i]]
        return my_sum