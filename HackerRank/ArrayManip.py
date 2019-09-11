#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    for command in queries:
        arr[command[0]] += command[2]
        if(command[1] + 1 < len(arr)):
            arr[command[1] + 1] -= command[2]
    runningTotal = 0
    maxValue = 0
    for x in arr:
        runningTotal += x
        if(runningTotal > maxValue):
            maxValue = runningTotal
    return maxValue
        
if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)
    print(result)
