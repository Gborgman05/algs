class Solution:
    def reverseDegree(self, s: str) -> int:
        sm = 0
        for i in range(len(s)):
            sm += (26 - ord(s[i]) + ord('a')) * (i + 1)
        return sm