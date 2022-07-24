# kind of dp with the check the last character position.
# not fully sure where to put it
# https://leetcode.com/problems/isomorphic-strings/submissions/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
#         need to create some kind of footprint for the items
        prev = {}
        seen = {}
        seen2 = {}
        prev2 = {}
        for i in range(len(s)):
            if s[i] not in seen:
                if t[i] not in seen2:
                    seen[s[i]] = 0
                    seen2[t[i]] = 0 
                    prev[s[i]] = i
                    prev2[t[i]] = i
                else:
                    return False
            else:
                if t[i] in seen2 and prev[s[i]] == prev2[t[i]]:
#                     check prev
                    prev[s[i]] = i
                    prev2[t[i]] = i
                else:
                    return False
        return True
                    