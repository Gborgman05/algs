class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = {}
        start = 0
        curr = 0
        max_len = 0
        if s:
            max_len = 1
        while curr < len(s):
            while curr < len(s) and s[curr] in store:
                store[s[start]] -= 1
                if store[s[start]] == 0:
                    del store[s[start]]
                start += 1
                
            # print(curr)
            while curr < len(s) and s[curr] not in store:
                store[s[curr]] = 1
                curr += 1
                # print(curr)
                # print(start)
                # print()
                # print(store)
                if curr <= len(s):
                    max_len = max(max_len, curr - start)
        return max_len

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        store = {}
        l = 0
        r = 0
        max_len = 1
        store[s[0]] = 1
        while r + 1 < len(s):
            while s[r+1] in store:
                store[s[l]] -= 1
                if store[s[l]] == 0:
                    del store[s[l]]
                l += 1
            store[s[r+1]] = 1
            r += 1
            max_len = max(r - l + 1, max_len)
        return max_len

