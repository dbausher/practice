"""http://practice.geeksforgeeks.org/problems/prime-number/0"""

import fileinput
import math

inputLines = fileinput.input()

testCases = int(inputLines.readline())

for l in range(testCases):
    n = int(inputLines.readline())
    primality = "Yes"
    for i in range(2,n):
        if not pow(i,n-1,n) == 1:
            primality = "No"
    print(primality)
