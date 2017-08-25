"""http://practice.geeksforgeeks.org/problems/faithful-numbers/0"""

import fileinput
import math
import collections

inputLines = fileinput.input()

testCases = int(inputLines.readline())


for l in range(testCases):
    n = int(inputLines.readline())
    binary = str(bin(n)[2:])
    out = 0
    for i in reversed(range(len(binary))):
        if binary[i] == '1':
            out += pow(7,len(binary) - 1 - i)


    print(out)
