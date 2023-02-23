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
    ans = [0.0]*(n+1)
    for i in range(len(queries)):
        ans[(queries[i][0])-1] += queries[i][2]
        ans[queries[i][1]] -= queries[i][2]
    for i in range(1,len(ans) - 1):
        ans[i]+=ans[i -1]
    max_ = float("-inf")
    for x in ans:
        max_= max(max_,x)
    return int(max_)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
