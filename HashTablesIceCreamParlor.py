#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    costMap = {}
    for i in range(len(cost)):
        if (money - cost[i]) in costMap:
            print(str(costMap[money-cost[i]]) + " " + str(i+1))
            return
        costMap[cost[i]] = i + 1


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
