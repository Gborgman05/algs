class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        balls = []
        for i in range(len(grid[0])):
            x = i
            y = 0
            above = True
            while True:
                if above:
                    if grid[y][x] == 1 and x < len(grid[y]) - 1:
                        if grid[y][x + 1] == -1:
                            balls.append(-1)
                            break
                        else:
                            x += 1
                            above = False
                    elif grid[y][x] == -1 and x > 0:
                        if grid[y][x - 1] == 1:
                            balls.append(-1)
                            break
                        else:
                            x -= 1
                            above = False
                    else:
                        balls.append(-1)
                        break
                else:
                    y += 1
                    if y == len(grid) - 1:
                        balls.append(x - 1)
                        break
                    else:
                        above = True
        return balls
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        balls = []
        for i in range(len(grid[0])):
            x = i
            y = 0
            above = True
            while True:
                if above:
                    if grid[y][x] == 1 and x < len(grid[y]) - 1:
                        if if grid[y][x + 1] == -1:
                            balls.append(-1)
                            break
                        else:
                            x += 1
                            above = False
                    elif grid[y][x] == -1 and x > 0:
                        if grid[y][x - 1] == 1:
                            balls.append(-1)
                            break
                        else:
                            x -= 1
                            above = False
                    else:
                        balls.append(-1)
                            break
                else:
                    y += 1
                    if y == len(grid) - 1:
                        balls.append(1):
                        break
                    else:
                        above = True
        return balls
