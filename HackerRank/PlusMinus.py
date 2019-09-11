#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for num in arr:
        if(num > 0):
            positive += 1
        elif (num < 0):
            negative += 1
        else:
            zero += 1
    print(str(round(positive/len(arr), 6)))
    print(str(round(negative/len(arr), 6)))
    print(str(round(zero/len(arr), 6)))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
