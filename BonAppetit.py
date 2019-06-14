#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    sum = 0
    for price in bill:
        sum += price
    sum -= bill[k]
    actualAmount = sum / 2
    if (actualAmount == b):
        print("Bon Appetit")
    else:
        print(str(int(b - actualAmount)))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
