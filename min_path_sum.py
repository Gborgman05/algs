class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        i, j = 0, 0
        while j < len(grid[0]):
            if i > 0 and j > 0:
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
            elif i > 0:
                print(i, j)
                grid[i][j] = grid[i-1][j] + grid[i][j]
            elif j > 0:
                grid[i][j] = grid[i][j-1] + grid[i][j]
            else:
                pass #at start
            if i == len(grid) - 1:
                i = 0
                j += 1
            else:
                i += 1
        return grid[-1][-1]
