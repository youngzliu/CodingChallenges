#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    min = 999999
    for i in range(len(arr) - 1):
        diff = arr[i+1] - arr[i]
        if (diff == 0):
            return 0
        if(diff < min):
            min = diff
    return min

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
