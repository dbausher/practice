"""http://practice.geeksforgeeks.org/problems/longest-increasing-subsequence/0"""

import fileinput
import collections

def LISS(l, upper):
    if(len(l) == 0):
        return 0
    if((tuple(l), upper) in memo):
        return memo[(tuple(l), upper)]
    curr = l[len(l) - 1]
    if(curr < upper):
        value = max(LISS(l[:len(l) - 1],curr) + 1,LISS(l[:len(l) - 1], upper))
        memo[(tuple(l), upper)] = value
        return value
    else:
        return LISS(l[:len(l) - 1], upper)

inputLines = fileinput.input()

testCases = int(inputLines.readline())

for l in range(testCases):
    listLength = inputLines.readline()
    numberList = list(map(int,inputLines.readline().strip().split()))
    memo = collections.defaultdict(list)
    memo[((), 1001)].append((1001,0))

    print(LISS(numberList,1001))