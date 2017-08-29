"""http://practice.geeksforgeeks.org/problems/product-of-primes/0"""

import fileinput
import math
import collections
import functools
import string

inputLines = fileinput.input()

testCases = int(inputLines.readline())

#turns out this doesn't work, it just pushes the punctuation to the far right
# def reverser(s):
#     if len(s) <= 1:
#         return s
#     if s[-1] in string.punctuation:
#         return reverser(s[:-1]) + s[-1]
#     else:
#         return s[-1] + reverser(s[:-1])

for l in range(testCases):
    boyos = inputLines.readline().strip()
    boy2 = ["" for i in range(len(boyos))]
    for i in range(len(boyos)):
        if boyos[i] in string.punctuation:
            boy2[i] = boyos[i]
    print(boyos)
    print(boy2)
    insertSpot = 0
    for j in reversed(range(0,len(boyos))):
        if boyos[j] not in string.punctuation:
            while(boy2[insertSpot] != ""):
                insertSpot += 1
            boy2[insertSpot] = boyos[j]
            
    print("".join(boy2))
