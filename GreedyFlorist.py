#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort()
    index = len(c) - 1
    cost = 0
    multiplier = 1
    while(index >= 0):
        for x in range(k):
            if(index < 0):
                return cost
            cost += c[index] * multiplier
            index -= 1
        multiplier += 1
    return cost
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
