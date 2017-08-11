"""http://practice.geeksforgeeks.org/problems/0-1-knapsack-problem/0"""

import fileinput

inputLines = fileinput.input()

testCases = int(inputLines.readline())

def knap(curr, space):
    if(curr == n or space <= 0):
        return 0
    if((curr,space) in memo):
        return memo[(curr,space)]
    if(space >= weightList[curr]):
        value = max(knap(curr + 1, space - weightList[curr]) + valueList[curr], knap(curr+1,space))
    else:
        value = knap(curr+1,space)
    memo[(curr,space)] = value
    return value


for l in range(testCases):
    n = int(inputLines.readline())
    w = int(inputLines.readline())
    valueList = list(map(int,inputLines.readline().strip().split()))
    weightList = list(map(int,inputLines.readline().strip().split()))


    memo = {}

    print(knap(0,w))