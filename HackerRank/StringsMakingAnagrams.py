#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    deletions = 0
    countsA = {}
    countsB = {}
    for char in a:
        if char in countsA:
            countsA[char] += 1
        else:
            countsA[char] = 1
    for char in b:
        if char in countsB:
            countsB[char] += 1
        else:
            countsB[char] = 1
    for char in countsA:
        if char in countsB:
            if countsA[char] > countsB[char]:
                countsA[char] -= countsB[char]
                countsB[char] = 0
            elif countsA[char] < countsB[char]:
                countsB[char] -= countsA[char]
                countsA[char] = 0
            else:
                countsA[char] = 0
                countsB[char] = 0
    for char in countsA:
        deletions += countsA[char]
    for char in countsB:
        deletions += countsB[char]
    return deletions



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
