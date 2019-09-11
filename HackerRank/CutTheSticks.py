#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    arr.sort()
    amountSticks = [len(arr)]
    for i in range(0, len(arr) - 1):
        if (arr[i+1] != arr[i]):
            amountSticks.append(len(arr) - (i + 1))
    return amountSticks
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
