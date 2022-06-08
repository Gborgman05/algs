#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/save-the-prisoner/problem?isFullScreen=false
#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#
# O(1) solution
def saveThePrisoner(n, m, s):
    # Write your code here
    offset = (m - 1) % n
    final = s + offset
    if final > n:
        final -= n
    return final

# O(n) solution
# def saveThePrisoner(n, m, s):
    # Write your code here
    # counter = s
    # candy_left = m
    # while candy_left != 1:
        # counter += 1       
        # if counter > n:
            # counter = 1
        # candy_left -= 1
    # return counter
    
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
