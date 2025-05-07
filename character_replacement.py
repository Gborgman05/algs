class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        curr = {}
        maxi = 0
        def valid(chars, k):
            if not chars:
                return True
            else:
                items = sorted(chars.items(), key=lambda a: a[1], reverse=True)
                total = 0
                for item in items[1:]:
                    total += item[1]
                return total <= k


        while l <= r and r < len(s):
            if s[r] in curr:
                curr[s[r]] += 1
            else:
                curr[s[r]] = 1
            while not valid(curr, k):
                if s[l] in curr:
                    curr[s[l]] -= 1
                    if curr[s[l]] == 0:
                        del curr[s[l]]
                l += 1
            maxi = max(maxi, r - l + 1)
            r += 1
        return maxi