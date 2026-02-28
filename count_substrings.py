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
        

class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return ""
        longest = s[0]
        c = 0
        for i in range(len(s)):
            modifier = 0
            while modifier + i < len(s) and -modifier + i >= 0 and s[i + modifier] == s[i - modifier]:
                modifier += 1
            # print(modifier , " ")
            c += 1 + modifier - 1
            

        for i in range(len(s)-1):
            modifier = 0
            while modifier + i+1 < len(s) and -modifier + i >= 0 and s[i + modifier+1] == s[i - modifier]:
                modifier += 1
            c += 1 + modifier - 1
        return c
