#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    maxval = 0
    nums = [0 for i in range(n)]
    # print(queries)
    for query in queries:
        start = query[0] - 1
        end = query[1]
        value = query[2]
        for i in range(start, end):
            nums[i] += value
            if nums[i] > maxval:
                maxval = nums[i]
        # print(nums)
    return maxval
