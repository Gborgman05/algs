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