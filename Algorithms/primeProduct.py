"""http://practice.geeksforgeeks.org/problems/product-of-primes/0"""

import fileinput
import math
import collections
import functools

inputLines = fileinput.input()

testCases = int(inputLines.readline())


for l in range(testCases):
    s, n = list(map(int,inputLines.readline().strip().split()))
    root = int(math.sqrt(n+1)) + 1
    pri = {i:True for i in range(3,root,2)}
    pri[2] = True
    out = {i:True for i in range(s,n+1)}
    for i in range(3,root):
        if i in pri:
            for j in range(2*i,root,i):
                pri.pop(j,None)
    for i in pri:
        div = s//i
        for j in range(i*div,n+1,i):
            if j!= i:
                out.pop(j,None)


    prod = functools.reduce(lambda x,y : (x*y)%(10**9+7),out)
    print(prod)
