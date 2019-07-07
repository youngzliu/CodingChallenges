#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    counts = {}
    numOdd = 0
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    for charCount in counts.values():
        if(charCount % 2 == 1):
            numOdd += 1
            if(numOdd > 1):
                return "NO"
    return "YES"
        




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
