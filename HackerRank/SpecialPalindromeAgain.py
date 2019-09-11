#!/bin/python3

import math
import os
import random
import re
import sys

def ariSum(n):
    return int(((n+1)/2) * n)

# Complete the substrCount function below.
def substrCount(n, s):
    currentChar = s[0]
    changes = []
    for i in range(0, n):
        if (s[i] != currentChar):
            changes.append(i)
            currentChar = s[i]
    if (len(changes) == 0):
        return ariSum(n)
    else:
        palStrings = 0
        palStrings += ariSum(changes[0])
        for i in range(1, len(changes)):
            palStrings += ariSum(changes[i] - changes[i-1])
            if((changes[i] - changes[i-1] == 1) and (s[changes[i]] == s[changes[i] - 2])):
                if(len(changes) == 2):
                    palStrings += min(changes[i-1], n - changes[i])
                elif(i == 1):
                    palStrings += min(changes[i-1], changes[i+1] - changes[i])
                elif(i == len(changes) - 1):
                    palStrings += min(changes[i-1] - changes[i-2], n - changes[i])
                else:
                    palStrings += min(changes[i-1] - changes[i-2], changes[i+1] - changes[i])
        palStrings += ariSum(n - changes[len(changes) - 1])
        return palStrings
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
