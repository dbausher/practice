"""http://www.geeksforgeeks.org/count-number-of-ways-to-cover-a-distance/"""

import fileinput

inputLines = fileinput.input()

testCases = int(inputLines.readline())

def ways(i):
    if(i > n):
        return 0
    if(i == n):
        return 1
    if i in memo:
        return memo[i]
    value = ways(i+1) + ways(i+2) + ways(i+3)
    memo[i] = value
    return value

for l in range(testCases):
    n = int(inputLines.readline())
    memo = {}

    print(ways(0))
