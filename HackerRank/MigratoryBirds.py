#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    birdCount = {}
    birdIndex = 7
    currentMax = 0
    for bird in arr:
        if (bird in birdCount):
            birdCount[bird] += 1
        else:
            birdCount[bird] = 1
    for bird, count in birdCount.items():
        if(count == currentMax and bird < birdIndex):
            birdIndex = bird
        elif(count > currentMax):
            birdIndex = bird
            currentMax = count
    return birdIndex
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
