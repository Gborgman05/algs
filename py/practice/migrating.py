#!/bin/python3
# https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=false&h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    max_bird = arr[0]
    counts = {}
    for bird in arr:
        if bird in counts:
            counts[bird] += 1
        else:
            counts[bird] = 1
        if counts[bird] > counts[max_bird]:
            max_bird = bird
    # srted = list(counts.items())
    # srted.sort(key=lambda a: a[1])
    # print(srted)
    # max_index = srted[-1][1]
    # for bird, count in srted:
    #     if srted[1] == max_index:
    #         return bird
    return max_bird
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
