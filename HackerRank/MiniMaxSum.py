#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    max = 0
    min = sys.maxsize
    sum = 0
    for num in arr:
        sum += num
        if(num > max):
            max = num
        if(num < min):
            min = num
    print(str(sum - max) + " " + str(sum - min))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
