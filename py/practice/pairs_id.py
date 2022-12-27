#!/bin/python3
# https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=false&h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    pairs = 0
    pair_waiting = {sock:False for sock in ar}
    for sock in ar:
        if pair_waiting[sock]:
            pairs += 1
            pair_waiting[sock] = False
        else:
            pair_waiting[sock] = True
    return pairs
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
