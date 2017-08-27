"""http://practice.geeksforgeeks.org/problems/binary-representation/0"""

import fileinput
import math

inputLines = fileinput.input()

testCases = int(inputLines.readline())

for l in range(testCases):
    n = int(inputLines.readline())
    nstring = bin(n)[2:]
    while len(nstring) < 14:
        nstring = "0" + nstring
    print(nstring)
