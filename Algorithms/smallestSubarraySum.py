
"""http://practice.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x/0"""

import fileinput
import math
import collections
import functools

inputLines = fileinput.input()


testCases = int(inputLines.readline())
for l in range(testCases):
    n, s = list(map(int,inputLines.readline().strip().split()))
    numList = list(map(int,inputLines.readline().strip().split()))
    count = 0
    out = -1
    found = False
    while (not found) and (count < n):
        for i in range(n - count):
            if count == 0:
                if numList[i] > s:
                    out = count + 1
                    found = True
            elif sum(numList[i:i+count]) > s:
                out = count
                found = True
                break
        count += 1

    print(out)