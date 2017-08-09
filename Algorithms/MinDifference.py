"""http://practice.geeksforgeeks.org/problems/minimum-sum-partition/0"""
import fileinput

inputLines = fileinput.input()

testCases = int(inputLines.readline())


def MSP(l1sum,curr):
    if((l1sum,curr) in memo):
        return memo[(l1sum,curr)]

    if(len(listboy) == curr):
        added = abs(sumBoy - 2*l1sum)
        memo[(l1sum,curr)] = added
        return added

    value = min(MSP(l1sum + listboy[curr], curr + 1),MSP(l1sum, curr + 1))
    memo[(l1sum,curr)] = value
    return value

for l in range(testCases):
    n = int(inputLines.readline())
    listboy = list(map(int, inputLines.readline().strip().split()))
    sumBoy = sum(listboy)
    memo = {}

    print(MSP(0,0))