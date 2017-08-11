"""http://practice.geeksforgeeks.org/problems/tom-and-jerry/0"""

import fileinput
import math

inputLines = fileinput.input()

testCases = int(inputLines.readline())

def mods(x):
    factors = set()
    for i in range(1,int(math.sqrt(x) + 1)):
        if(x%i == 0):
            factors.add(i)
            if not i==1:
                factors.add(x//i)
    return factors

def canWin(curr):
    if(curr in memo):
        return memo[curr]
    value = False
    for i in mods(curr):
        ivalue = True
        sub = curr-i
        if sub in memo:
            ivalue = not memo[sub]
        else:
            for j in mods(sub):
                if not canWin(sub-j):
                    ivalue = False
                    memo[sub] = True
                    break
        if ivalue:
            memo[sub] = False
            value = True
            break
    memo[curr] = value
    return value

for l in range(testCases):
    n = int(inputLines.readline())
    memo = {0:False,1:False,2:True}
    print(int(canWin(n)))