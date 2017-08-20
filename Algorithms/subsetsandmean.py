"""http://practice.geeksforgeeks.org/problems/number-of-subsets-and-mean/0"""

import fileinput
import math

inputLines = fileinput.input()

testCases = int(inputLines.readline())

for l in range(testCases):
    n = int(inputLines.readline())
    numList = list(map(int,inputLines.readline().strip().split()))
    maxcount = pow(2,numList.count(max(numList)),10**9 + 7) - 1
    mincount = pow(2,numList.count(min(numList)),10**9 + 7) - 1
    print(str(maxcount) + " " + str(mincount))
