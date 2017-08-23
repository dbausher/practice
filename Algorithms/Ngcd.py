"""http://practice.geeksforgeeks.org/problems/gcd-of-array/0"""

import fileinput
import math
import functools

inputLines = fileinput.input()

testCases = int(inputLines.readline())

def euclid(a,b):
    while b:
        a,b = b,a%b
    return a


for l in range(testCases):
    n = int(inputLines.readline())
    numList = list(map(int,inputLines.readline().strip().split()))



    print(functools.reduce(euclid,numList))
