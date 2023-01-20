#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    k=0
    for x in range(len(a)-1):
        for y in range((n-1)-x):
            if a[y]>a[y+1]:
                temp =a[y]
                a[y]=a[y+1]
                a[y+1]=temp
                k=k+1
    print(f'Array is sorted in {k} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[len(a)-1]}')

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
