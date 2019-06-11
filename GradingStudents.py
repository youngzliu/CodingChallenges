#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    roundedGrades = []
    for grade in grades:
        if (grade < 38):
            roundedGrades.append(grade)
        else:
            if(grade % 5 > 2):
                roundedGrades.append(grade + (5 - (grade % 5)))
            else:
                roundedGrades.append(grade)
    return roundedGrades

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
