
"""http://practice.geeksforgeeks.org/problems/pythagorean-triplet/0"""

import fileinput
import math
import collections
import functools

inputLines = fileinput.input()

testCases = int(inputLines.readline())
for l in range(testCases):
    n = int(inputLines.readline().strip())
    numList = list(map(lambda x : int(x)**2,inputLines.readline().strip().split()))
    numset = set(numList)

    count = 0

    for i in range(len(numList) - 1):
        out = "No"
        for j in range(i+1,len(numList)):
            if numList[i] + numList[j] in numset:
                out = "Yes"
                break
        if out == "Yes":
            break
    print(out)