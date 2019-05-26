#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sums = []
    for x in range(1, len(arr) - 1):
        for y in range(1, len(arr[x]) - 1):
            sum = 0
            sum += arr[x-1][y+1]
            sum += arr[x][y+1]
            sum += arr[x+1][y+1]
            sum += arr[x][y]
            sum += arr[x-1][y-1]
            sum += arr[x][y-1]
            sum += arr[x+1][y-1]
            sums.append(sum)
    return max(sums)


if __name__ == '__main__':
  

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(result)
