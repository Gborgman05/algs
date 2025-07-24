class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            for w in wordDict:
                start = i - len(w)
                if start >= 0 and dp[start] and s[start:i] == w:
                    dp[i] = True
                    break
        
        return dp[-1]

    class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # iterate over string, checking wordDict each time
        can_make = [False] * (len(s)+ 1)
        can_make[0] = True

        for i in range(len(s)):
            if can_make[i]:
                for word in wordDict:
                    # print(s[i:i+len(word)])
                    # print(i + len(word))
                    if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                        can_make[i +len(word)] = True
        # print( can_make )
        return can_make[-1]

        