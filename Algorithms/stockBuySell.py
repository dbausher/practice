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
    
    out = []
    currmin = 0
    currmax = -1
    for i in range(n-1):
        if numList[i] < numList[i+1]:
            currmax = i+1
        else:
            if currmax != -1:
                out.append((currmin,currmax))
                currmax = -1
            currmin = i+1
    if currmax != -1:
        out.append((currmin,n-1))


    if len(out) > 0:
        outstr = ""
        for j,k in out:
            outstr += "(" + str(j) + " " + str(k) + ") "
        print(outstr[:-1])
    else:
        print("No Profit")

