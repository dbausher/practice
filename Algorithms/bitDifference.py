"""http://practice.geeksforgeeks.org/problems/bit-difference/0"""

import fileinput
import math

inputLines = fileinput.input()

testCases = int(inputLines.readline())

for l in range(testCases):
    n1,n2 = list(map(int,inputLines.readline().strip().split()))
    switch  = bin(~n1 & n2).count("1") + bin(n1 & ~n2).count("1")
    print(switch)
