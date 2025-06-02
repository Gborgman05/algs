class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    #print(max_area)
                    q = [(i, j)]
                    size = 0
                    while q:
                        curr = q.pop(0)
                        x = curr[0]
                        y = curr[1]
                        size += 1
                        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != 1:
                            size -= 1
                            continue
                        q.append((x+1, y))
                        q.append((x-1, y))
                        q.append((x, y+1))
                        q.append((x, y-1))
                        grid[x][y] = "x"
                    max_area = max(max_area, size)
        return max_area

        