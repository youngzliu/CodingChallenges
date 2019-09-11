#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    luck = 0
    impContests = []
    for contest in contests:
        if contest[1] == 0:
            luck += contest[0]
        if contest[1] == 1:
            impContests.append(contest[0])
    impContests.sort()
    for i in range(len(impContests) - 1, len(impContests) - k - 1, -1):
        if(i >= 0):
            luck += impContests[i]
    for i in range(len(impContests) - k - 1, -1, -1):
        if(i >= 0):
            luck -= impContests[i]
    return luck


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
