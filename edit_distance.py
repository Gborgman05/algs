class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dfs = [[0 for i in range(len(word2))] for j in range(len(word1))]
        dfs = {}
        def recurse(i, j):
            if (i, j) in dfs:
                return dfs[(i, j)]
            else:
                if i == len(word1) and j == len(word2):
                    dfs[(i, j)] = 0
                elif i == len(word1):
                    dfs[(i, j)] = len(word2) - j
                elif j == len(word2):
                    dfs[(i, j)] = len(word1) - i
                else:
                    if word1[i] == word2[j]:
                        dfs[(i, j)] = recurse(i+1, j+1)
                    else:
                        res = min(recurse(i, j+1), recurse(i+1, j))
                        res = min(res, recurse(i+1, j+1))
                        dfs[(i, j)] = res + 1
            return dfs[(i, j)]
        return recurse(0, 0)
        