class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            return l >= 0 and r < len(s)  and s[l] == s[r]
        final = 0
        final_str = ""

        for i in range(len(s)):
            l = i - 1
            r = i + 1
            total_len = 1
            while expand(l, r):
                total_len += 2
                l -= 1
                r += 1
            if total_len > final:
                #print(s[l+1:r-1])

                final = total_len
                final_str = s[l+1:r]
            if i + 1 < len(s) and s[i]==s[i+1]:
                l = i - 1
                r = i + 2
                total_len = 2
                while expand(l, r):
                    total_len += 2
                    l -= 1
                    r += 1
                if total_len > final:
                    final = total_len
                    final_str = s[l+1:r]

        return final_str

