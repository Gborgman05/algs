class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        store = {}
        final = 0
        def dfs(i, j):
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0

            if (i, j) in store:
                return store[(i, j)]
                
            if s[i] == t[j]:
                tmp = dfs(i+1, j)
                store[(i, j)] = tmp + dfs(i+1, j+1)
                return store[(i, j)]
            else:
                store[(i, j)] = dfs(i+1, j)
                return store[(i, j)]
        return dfs(0, 0)





        