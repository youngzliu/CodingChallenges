#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    countDict = {}
    for char in s:
        if char in countDict:
            countDict[char] += 1
        else:
            countDict[char] = 1
    countList = list(countDict.values())
    countList.sort()
    if (countList[0] == countList[len(countList)-1]):
        return "YES"
    elif(countList[0] == 1 and countList[1] == countList[len(countList)-1]):
        return "YES"
    elif(countList[0] == countList[len(countList) - 2] and countList[len(countList) - 2] + 1 == countList[len(countList) - 1]):
        return "YES"
    else:
        return "NO"
    
    




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

