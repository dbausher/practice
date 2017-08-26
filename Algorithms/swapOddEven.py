"""http://practice.geeksforgeeks.org/problems/prime-number/0"""

import fileinput
import math

inputLines = fileinput.input()

testCases = int(inputLines.readline())

for l in range(testCases):
    n = int(inputLines.readline())
    odds = 0
    evens = 0
    for i in range(0,33,2):
        evens += pow(2,i)
    for i in range(1,33,2):
        odds += pow(2,i)
    print(((n & odds) << 1) | ((n & evens) >> 1))
