"""http://practice.geeksforgeeks.org/problems/convert-array-into-zig-zag-fashion/0"""

import fileinput
import math
import functools

inputLines = fileinput.input()

testCases = int(inputLines.readline())



for l in range(testCases):
    n = int(inputLines.readline())
    numList = list(map(int,inputLines.readline().strip().split()))
    greater = False
    for i in range(len(numList) - 1):
        if (numList[i] > numList[i + 1]) != greater:
            numList[i],numList[i+1] = numList[i+1],numList[i]
        greater = not greater
    print(" ".join(list(map(str,numList))))