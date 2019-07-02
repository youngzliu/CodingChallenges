#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    permArray = []
    indexDict = {}
    for i in range(len(p)):
        indexDict[p[i]] = i + 1
    for num in range(1, len(p) + 1):
        firstIndex = indexDict[num]
        secondIndex = indexDict[firstIndex]
        permArray.append(secondIndex)
    return permArray
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
