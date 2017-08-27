"""http://practice.geeksforgeeks.org/problems/count-total-set-bits/0"""

import fileinput
import math

inputLines = fileinput.input()

testCases = int(inputLines.readline())

for l in range(testCases):
    n = int(inputLines.readline())
    out = 0
    for i in range(n + 1):
        out += bin(i).count("1")
    print(out)