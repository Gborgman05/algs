class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = 0
        r = 0
        max_substr = 0
        for i in range(len(s)):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:
                max_substr = max(max_substr, l*2)
            elif r > l:
                l=r=0
        l, r = 0, 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:
                max_substr = max(max_substr, l*2)
            elif r < l:
                l=r=0
        return max_substr
