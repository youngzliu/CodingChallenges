#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    ele = 0
    valleys = 0
    state = 0
    if s[0] == "U":
        state = 1
        ele = 1
    else:
        state = -1
        ele = -1
    for x in range(1, len(s)):
        if(s[x] == "U"):
            ele += 1
        else:
            ele -= 1
        if(ele == 0):
            if (state == -1):
                valleys += 1
            if(x != len(s) - 1):
                if (s[x+1] == "U"):
                    state = 1
                else:
                    state = -1
    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
