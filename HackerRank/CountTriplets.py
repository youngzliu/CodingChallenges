#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    countDict = {}
    triplets = 0
    for num in arr:
        if (num, 1) in countDict:
            countDict[(num, 1)] += 1
        else:
            countDict[(num, 1)] = 1
        if (num / r, 1) in countDict:
            if (num, 2) in countDict:
                countDict[(num, 2)] += countDict[(num/r, 1)]
            else:
                countDict[(num, 2)] = countDict[(num/r, 1)]
        if (num / r, 2) in countDict:
            triplets += countDict[(num/r, 2)]
    return triplets

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
