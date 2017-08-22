"""http://practice.geeksforgeeks.org/problems/sieve-of-eratosthenes/0"""

import fileinput
import math
import collections

inputLines = fileinput.input()

testCases = int(inputLines.readline())


for l in range(testCases):
    n = int(inputLines.readline())
    out = {i:True for i in range(1,n+1)}
    for i in range(2,n + 1):
        if i in out:
            for j in range(2*i,n+1,i):
                out.pop(j,None)


    print(" ".join(list(map(str,out))))
