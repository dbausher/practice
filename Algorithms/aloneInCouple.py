"""http://practice.geeksforgeeks.org/problems/product-of-primes/0"""

import fileinput
import math
import collections
import functools

inputLines = fileinput.input()

testCases = int(inputLines.readline())


for l in range(testCases):
    n = int(inputLines.readline())
    numList = list(map(int,inputLines.readline().strip().split()))
    xor = functools.reduce(lambda x,y : x^y,numList)
    print(xor)
