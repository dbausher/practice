"""http://practice.geeksforgeeks.org/problems/longest-increasing-subsequence/0"""

import fileinput
import collections

def LISS(end):
    if(end in memo):
        return memo[end]
    curr = numberList[end]
    value = 1
    for j in reversed(range(end)):
        if(numberList[j] < curr):
            jvalue = LISS(j) + 1
            if(jvalue > value):
                value = jvalue
    memo[end] = value
    return value

inputLines = fileinput.input()

testCases = int(inputLines.readline())

for l in range(testCases):
    listLength = int(inputLines.readline())
    numberList = list(map(int,inputLines.readline().strip().split()))
    memo = {}
    memo[0] = 1

    length = 0

    for i in range(listLength):
        ival = LISS(i)
        if (ival > length):
            length = ival 

    print(length)