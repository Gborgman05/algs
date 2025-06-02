class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # first detect if there are any isolated unspoiled oranges
        # copy = grid[:]
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if copy[i][j] == 2:
        #             q = [(i, j)]
        #             while q:
        #                 curr = q.pop()
        #                 x = curr[0]
        #                 y = curr[1]
        #                 if x < 0 or y < 0 or x >= len(grid) or y >= len(copy[0]) or copy[x][y] == 3 or copy[x][y] == 0 :
        #                     continue
        #                 copy[x][y] = 3
        #                 q += [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        count_not_rotten = 0
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # if copy[i][j] == 1:
                #     return -1
                if grid[i][j] == 1:
                    count_not_rotten += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        print(grid)
        step = 0
        print(count_not_rotten)
        print(q)
        while count_not_rotten > 0:
            # or you could go here until the q is empty and there are still not rotten oranges, skipping the first
            step += 1
            next_step = []
            if not q:
                return -1
            while q:
                curr = q.pop(0)
                x = curr[0]
                y = curr[1]
                if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 3 or grid[x][y] == 0 :
                    continue
                if grid[x][y] == 1:
                    count_not_rotten -= 1
                grid[x][y] = 3 
                next_step += [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            q = next_step
            
        if step > 0:
            return step - 1

        return step