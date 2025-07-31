class Solution:
    def reverse(self, x: int) -> int:
        val = ""
        if x < 0:
            val = val + "-"
            x = str(-x)
        else:
            x = str(x)
        for char in x[::-1]:
            val += char
        val = int(val)
        return val if (val <= (2 ** 31 - 1) and val >= ((-2) ** 31 )) else 0 
        
