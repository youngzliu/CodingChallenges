#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    newString = ""
    if(s[0:2] == "12" and s[-2:] == "AM"):
        newString += "00"
        newString += s[2:-2]
    elif(s[0:2] != "12" and s[-2:] == "PM"):
        newString += str(int(s[0:2]) + 12)
        newString += s[2:-2]
    else:
        newString = s[0:-2]
    return newString
    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
