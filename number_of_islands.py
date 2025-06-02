class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    #do dfs on this and mark all as seen x
                    q= [(i, j)]
                    count += 1
                    #print("break")
                    while q:
                        #print(q)
                        curr = q.pop(0)
                        x = curr[0]
                        y = curr[1]
                        #print(grid)
                        if x < 0 or x >=len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != "1":
                            continue
                        #print(grid[x][y])
                        grid[x][y] = "x"
                        q.append((x+1, y))
                        q.append((x-1, y))
                        q.append((x, y+1))
                        q.append((x, y-1))
        return count
                        
        