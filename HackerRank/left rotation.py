#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    rotations = d % len(a)
    newList = [None] * len(a)
    for x in range(0, len(a) - rotations):
        newList[x] = a[x + rotations]
    for x in range(len(a) - rotations, len(a)):
        newList[x] = a[x - (len(a) - rotations)]
    return newList





if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(result)