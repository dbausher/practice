"""http://practice.geeksforgeeks.org/problems/sort-the-array/0"""

import fileinput
import math

inputLines = fileinput.input()

testCases = int(inputLines.readline())

for l in range(testCases):
    n = int(inputLines.readline())
    numList = list(map(int,inputLines.readline().strip().split()))

    # correct = False

    # while(not correct):
    #     for i in range(n -1):
    #         first = numList[i]
    #         second = numList[i+1]
    #         if(first > second):
    #             numList[i] = second
    #             numList[i+1] = first
    #             break
    #     else:
    #         correct = True

    print(" ".join(list(map(str,sorted(numList)))))