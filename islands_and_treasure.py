class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def bfs(i, j, prev):
            q = collections.deque()
            q.append((i, j, -1))
            while q:
                x, y, prev_val = q.popleft()
                if grid[x][y] >= 0:
                    if grid[x][y] < prev_val + 1:
                        continue
                    grid[x][y] = min(grid[x][y], prev_val + 1)
                    for d in direct:
                        dx, dy = d[0], d[1]
                        if x + dx < m and x + dx >= 0 and y + dy < n and y + dy >= 0:
                            q.append((x+dx, y+dy, grid[x][y]))
                        


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    bfs(i, j, -1)
        