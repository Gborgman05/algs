# counts the number of "1" islands on a grid using dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) < 1:
            return 0
        count = 0
        def dfs(cell_x, cell_y):
            if cell_x < 0 or cell_y < 0 or cell_x >= len(grid) or cell_y >= len(grid[0]) or grid[cell_x][cell_y] != "1":
                return
            else:
                grid[cell_x][cell_y] = "2"
                dfs(cell_x - 1, cell_y)
                dfs(cell_x , cell_y - 1)
                dfs(cell_x + 1, cell_y)
                dfs(cell_x , cell_y + 1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count
        
                    
                    
        