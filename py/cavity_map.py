#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    # Write your code here
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[i]) - 1:
                pass
            else:
                cur = int(grid[i][j])
                cav = True
                for k, l in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    if grid[i+k][j+l] == 'X' or int(grid[i+k][j+l])>=cur:
                        cav = False
                        break
                if cav:
                    tmp = list(grid[i])
                    tmp[j] = "X"
                    grid[i] = "".join(tmp)
    return grid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
