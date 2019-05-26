#!/bin/python3

import math
import os
import random
import re
import sys

amtSwaps = 0
arr = []

def swap(x, y):
    global amtSwaps
    global arr
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp
    amtSwaps += 1
    
def perfectSwap(x):
    global arr
    if arr[arr[x]] == x:
        swap(x, arr[x]) 

def minimumSwaps(inputArr):
    global arr
    global amtSwaps
    arr = inputArr
    for x in range(len(arr)):
        if (arr[x] != x):
            perfectSwap(x)
    
    return amtSwaps

if __name__ == '__main__':

    n = int(input())

    inputArr = list(map(int, input().rstrip().split()))
    inputArr.insert(0, 0)

    res = minimumSwaps(inputArr)
    print(res)
    print(arr)
