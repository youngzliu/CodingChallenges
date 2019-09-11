#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    wordDict = {}
    for word in magazine:
        if (word not in wordDict):
            wordDict[word] = 1
        else:
            wordDict[word] += 1
    for word in note:
        if((word in wordDict) and (wordDict[word] != 0)):
            wordDict[word] -= 1
        else:
            return "No"
    return "Yes"


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
