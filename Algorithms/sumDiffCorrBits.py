"""http://practice.geeksforgeeks.org/problems/find-sum-of-different-corresponding-bits-for-all-pairs/0"""

import fileinput
import math
import functools

inputLines = fileinput.input()

testCases = int(inputLines.readline())



for l in range(testCases):
    n = int(inputLines.readline())
    numList = list(map(int,inputLines.readline().strip().split()))
    binCount = {}
    binCount[-1] = 0
    for i in range(31):
        for j in numList:
            if(pow(2,i) & j):
                if i in binCount:
                    binCount[i] += 1
                else:
                    binCount[i] = 1
    for j in numList:
        if j < 0:
            binCount[-1] += 1

    out = 0
    for k in binCount:
        v = binCount[k]
        out = (out + v*(n-v))%(10**9 + 7)
    print(2*out)
