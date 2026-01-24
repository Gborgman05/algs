class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        DP = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        for i in range(len(text2) - 1, -1, -1):
            for j in range(len(text1) - 1, -1, -1):
                if text1[j] == text2[i]:
                    DP[i][j] = 1 + DP[i+1][j+1]
                else:
                    DP[i][j] = max(DP[i+1][j], DP[i][j+1])
        return DP[0][0]

    class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """ 2d list, where first is representing where we are in first string, second is second string
        we iterate over the strings and check if the characters are the same otherwise we add to the index """
        longest_sequences = [[0] * (len(text2) + 1) for _ in range(len(text1)+1)]
        longest = 0
        for i in range(len(longest_sequences)):
            for j in range(len(longest_sequences[0])):
                local_longest = 0
                if i > 0:
                    local_longest = max(local_longest, longest_sequences[i-1][j])
                
                if j > 0:
                    local_longest = max(local_longest, longest_sequences[i][j-1])
                if j > 0  and i > 0 and text1[i-1] == text2[j-1]:
                    local_longest = max(local_longest, longest_sequences[i-1][j-1] + 1)
                
                longest_sequences[i][j] = local_longest
                longest = max(longest, local_longest)
        return longest
                    
