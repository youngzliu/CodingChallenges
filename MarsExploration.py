#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    difference = 0
    for i in range(len(s)):
        if((i+1) % 3 == 2):
            if(s[i] != "O"):
                difference += 1
        else:
            if(s[i] != "S"):
                difference += 1
    return difference






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
