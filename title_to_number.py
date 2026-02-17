class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        base = 1
        final = 0
        for i in range(len(columnTitle)-1, -1, -1):
            final += (ord(columnTitle[i]) - ord('A') + 1) * base
            base *= 26
        return final
