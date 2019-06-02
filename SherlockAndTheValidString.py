#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    countDict = {}
    difference = 0
    for char in s:
        if char in countDict:
            countDict[char] += 1
        else:
            countDict[char] = 1
    countList = list(countDict.values())
    base = countList[0]
    for i in range(1, len(countList)):
        difference += abs(base - countList[i])
        if(difference > 1):
            return "NO"
    return "YES"




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
