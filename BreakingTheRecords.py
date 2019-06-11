#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max = scores[0]
    min = scores[0]
    maxBroken = 0
    minBroken = 0
    for num in scores:
        if(num > max):
            max = num
            maxBroken += 1
        elif(num < min):
            min = num
            minBroken += 1
    return [maxBroken, minBroken]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
