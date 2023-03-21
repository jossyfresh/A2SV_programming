#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    new = ""
    def recur(n,l,r):
        mid = (l+r)//2
        if l == r:
            return int(n[l])
        x = recur(n,l,mid)
        y = recur(n,mid+1,r)
        z = x + y
        if z > 9:
            z = z-(9)
        return z
    new = str(recur(n,0,len(n)-1))*k
    return recur(new,0,len(new)-1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
