class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = {}
        cnt = 0
        max_count = 0
        l = 0
        for r in range(len(s)):
            while r >= l and s[r] in store:
                del store[s[l]]
                l += 1
            store[s[r]] = 1
            max_count = max(max_count, r - l  + 1)
        return max_count