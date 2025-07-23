class Solution:
    def countSubstrings(self, s: str) -> int:
        # ababca
        palindromes = 0
        for i in range(len(s)):
            l = 0
            r = 0
            while i+l >= 0 and r+i < len(s) and s[i+l] == s[r+i]:
                l -= 1
                r += 1
                palindromes += 1
            l = 0
            r = 1
            while i+l >= 0 and r+i < len(s) and s[i+l] == s[r+i]:
                l -= 1
                r += 1
                palindromes += 1
        return palindromes
        