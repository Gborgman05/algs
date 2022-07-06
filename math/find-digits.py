#!/bin/python3
# https://www.hackerrank.com/challenges/find-digits/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    saved = n
    count = 0
    while n != 0:
        digit = n % 10 
        print(digit)
        n -= digit
        n /= 10
        n = int(n)
        if  digit == 0:
            continue
        if saved % digit == 0:
            count += 1
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
