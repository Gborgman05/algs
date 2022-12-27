class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        mx = 0
        def check_dup(arr):
            store = {}
            for char in arr:
                if char in store:
                    return False
                else:
                    store[char] = 0
            return True
        while end < len(s):
            if check_dup(s[start:end]):
                if end - start > mx:
                    print(start)
                    print(end)
                    mx = end - start
                end += 1
            else:
                start += 1
        if end - start > mx and check_dup(s[start:end]):
            print(start)
            print(end)
            mx = end - start
        return mx
            
            
        