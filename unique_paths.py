class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j ==0:
                    grid[i][j] = 1
                elif i==0:
                    # print(grid)
                    # print(i)
                    # print(j)
                    grid[i][j] = grid[i][j-1]
                elif j == 0:
                    grid[i][j] = grid[i-1][j]
                else:
                    grid[i][j] = grid[i][j-1] + grid[i-1][j]
        # print(grid)
        return grid[-1][-1]
        