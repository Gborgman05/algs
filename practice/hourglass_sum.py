#!/bin/python3
# https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true
import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    my_max = None
    counter = 0
    for j in range(len(arr)):
        for i in range(len(arr[0])):
            if j - 1 < 0 or j + 1 >= len(arr) or i - 1 < 0 or i + 1 >= len(arr[0]):
                pass
            else:
                top = sum(arr[j-1][i-1:i+2])
                bot = sum(arr[j+1][i-1:i+2])
                my_sum = top + bot + arr[j][i]
                my_max = my_max if my_max != None and my_sum < my_max else my_sum
                counter += 1
                print(counter)
                print("value", my_sum)
                print("my sum", my_sum)
    return my_max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
