class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def expand(l, r):
            return l >= 0 and r < len(s) and s[l] == s[r]
        for i in range(len(s)):
            count += 1
            l = i - 1
            r = i + 1
            while expand(l, r):
                count += 1
                l -= 1
                r += 1
            
            if i + 1 < len(s) and s[i] == s[i+1]:
                count += 1
                l = i - 1
                r = i + 2
                while expand(l, r):
                    count += 1
                    l -= 1
                    r += 1
        return count

            