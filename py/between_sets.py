#Galen Borgman
#From hackerrank.com
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    possibly_between = []
    i = 0
    #print([1 for value in a])
    #print([((i * a[0]) % value) == 0 for value in a if i != 0])
    while i * a[0] <= b[0]:

        if all([((i * a[0]) % value) == 0 for value in a if i != 0]) and all([(value % (i * a[0])) == 0 for value in b if i != 0]):
            possibly_between.append(i * a[0])
        i += 1 
    possibly_between.remove(0)
    return len(possibly_between)
