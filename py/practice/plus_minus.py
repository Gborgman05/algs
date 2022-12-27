#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    neg = 0
    pos = 0
    z = 0
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            z += 1
    total = neg + pos + z
    print(round(pos / total, 6))
    print(round(neg / total, 6))
    print( round(z / total, 6))

        
    # Write your code here
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
