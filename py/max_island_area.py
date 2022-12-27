class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            if grid[y][x] == 1:
                grid[y][x] = -1
                sm = 1
                if y > 0:
                    sm += dfs(x, y-1)
                if x > 0:
                    sm += dfs(x-1, y)
                if y < len(grid) - 1:
                    sm += dfs(x, y+1)
                if x < len(grid[y]) -1:
                    sm += dfs(x+1, y)
                return sm
            else:
                return 0
        mx = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                m = dfs(j, i)
                if m > mx:
                    mx = m
        return mx
                