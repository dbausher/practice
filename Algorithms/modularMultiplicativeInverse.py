"""http://practice.geeksforgeeks.org/problems/modular-multiplicative-inverse/0"""

import fileinput
import math

inputLines = fileinput.input()

testCases = int(inputLines.readline())

for l in range(testCases):
    a,m = list(map(int,inputLines.readline().strip().split()))
    inverse = -1
    for i in range(m):
        if(m*i + 1)/a == (m*i + 1)//a and (m*i + 1)//a < m:
            inverse = (m*i + 1)//a
            break
    print(inverse)

