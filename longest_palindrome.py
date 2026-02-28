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

class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = s[0]
        for start in range(len(s)):
            i = 0
            while start - i >= 0 and start + i < len(s) and s[start-i] == s[start+i]:
                if len(l) < i * 2 + 1:
                    l = s[start-i:start+i+1]
                i += 1

            end = start + 1
            if end < len(s):
                i = 0
                while start - i >= 0 and end + i < len(s) and s[start-i] == s[end + i]:
                    if len(l) < i*2 + 2:
                        l = s[start-i:end+i+1]
                    i += 1
        return l

class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = s[0]
        for start in range(len(s)):
            i = 0
            while start - i >= 0 and start + i < len(s) and s[start-i] == s[start+i]:
                if len(l) < i * 2 + 1:
                    l = s[start-i:start+i+1]
                i += 1

            end = start + 1
            if end < len(s):
                i = 0
                while start - i >= 0 and end + i < len(s) and s[start-i] == s[end + i]:
                    if len(l) < i*2 + 2:
                        l = s[start-i:end+i+1]
                i += 1
        return l


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        longest = s[0]
        for i in range(len(s)):
            modifier = 0
            while modifier + i < len(s) and -modifier + i >= 0 and s[i + modifier] == s[i - modifier]:
                modifier += 1
            # print(modifier , " ")
            if 2*(modifier - 1) + 1 > len(longest):
                longest = s[i - (modifier-1):i + (modifier)]

        for i in range(len(s)-1):
            modifier = 0
            while modifier + i+1 < len(s) and -modifier + i >= 0 and s[i + modifier+1] == s[i - modifier]:
                modifier += 1
            print(modifier)
            if 2*(modifier - 1) + 2 > len(longest):
                longest = s[i - (modifier-1):i + (modifier+1)]
        return longest
