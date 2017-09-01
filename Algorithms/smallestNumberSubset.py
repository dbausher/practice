"""http://practice.geeksforgeeks.org/problems/smallest-number-subset/0"""

import fileinput
import math
import collections
import functools

inputLines = fileinput.input()


testCases = int(inputLines.readline())
for l in range(testCases):
    n = int(inputLines.readline().strip())
    numList = list(map(int,inputLines.readline().strip().split()))
    out = 1

    for i in range(n):
        if numList[i] > out:
            break
        else:
            out += numList[i]
    print(out)
