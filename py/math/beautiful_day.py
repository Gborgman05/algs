#!/bin/python3
# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    # Write your code here
    count = 0
    def invert_num(num):
        digit  = 1
        inverted = 0
        while num:
            inverted *= 10
            mydig = num % 10
            num -= mydig
            num /= 10
            inverted += mydig
        return int(inverted)
    for num in range(i, j+1):
        print(num - invert_num(num))
        if (num - invert_num(num)) % k == 0:
            count += 1
    return count
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
