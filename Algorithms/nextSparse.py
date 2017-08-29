"""http://practice.geeksforgeeks.org/problems/next-sparse-binary-number/0"""

import fileinput
import math

inputLines = fileinput.input()

testCases = int(inputLines.readline())

for l in range(testCases):
    n = int(inputLines.readline())
    while 1:
        if bin(n).count("11") == 0:
            print(n)
            break
        n += 1

