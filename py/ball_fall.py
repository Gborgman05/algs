# initial solution commented out below, didn't work
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        width = len(grid[0])
        height = len(grid)
        def go_left(x, y):
            if x < 1:
                return False
            return grid[y][x - 1] == -1 == grid[y][x]
        def go_right(x, y):
            if x >= width - 1:
                return False
            # print(y, " ", x)
            # print(len(grid[y]))
            return grid[y][x + 1] == 1 == grid[y][x]
        def dfs(x):
            y = 0
            while y < height:
                if go_left(x, y):
                    x -= 1
                    y += 1
                elif go_right(x, y):
                    x += 1
                    y += 1
                else:
                    return -1
            return x
        res = []
        for i in range(width):
            res.append(dfs(i))
        return res
                
        # balls = []
        # for i in range(len(grid[0])):
        #     x = i
        #     y = 0
        #     above = True
        #     while True:
        #         if above:
        #             if grid[y][x] == 1 and x < len(grid[y]) - 1:
        #                 if grid[y][x + 1] == -1:
        #                     balls.append(-1)
        #                     break
        #                 else:
        #                     x += 1
        #                     above = False
        #             elif grid[y][x] == -1 and x > 0:
        #                 if grid[y][x - 1] == 1:
        #                     balls.append(-1)
        #                     break
        #                 else:
        #                     x -= 1
        #                     above = False
        #             else:
        #                 balls.append(-1)
        #                 break
        #         else:
        #             y += 1
        #             if y == len(grid) - 1:
        #                 balls.append(x - 1)
        #                 break
        #             else:
        #                 above = True
        # return balls
