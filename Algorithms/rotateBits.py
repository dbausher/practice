"""http://practice.geeksforgeeks.org/problems/rotate-bits/0"""

import fileinput
import math
import collections
import functools

inputLines = fileinput.input()

testCases = int(inputLines.readline())

rol = lambda val, r_bits, max_bits: (val << r_bits%max_bits) & (2**max_bits-1) | ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

for l in range(testCases):
    n, r = list(map(int,inputLines.readline().strip().split()))
    r = r%16
    left = ((n << r) & (65535)) | ((n & (65535)) >> (16-r))
    right = ((n >> r) & (65535)) | ((n & (65535)) << (16-r))
    print(left)
    print(right)