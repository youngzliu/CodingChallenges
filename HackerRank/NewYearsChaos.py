#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    arr2 = []
    for x in range(len(q)):
        if (q[x] - x - 1) > 2:
            return "Too chaotic"
        elif (q[x] - x - 1) > 0:
            bribes += q[x]- x - 1
        else:
            arr2.append(q[x])
            bribes += numSwaps(arr2)
    return bribes

def numSwaps(alist):
    num = 0
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                num += 1
    return num

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
