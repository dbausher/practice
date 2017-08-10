"""http://practice.geeksforgeeks.org/problems/path-in-matrix/0"""

import fileinput

inputLines = fileinput.input()

testCases = int(inputLines.readline())

def findSum(r,c):
    if((r,c) in memo):
        return memo[r,c]
    if(r==n or c == n or c==-1):
        return 0

    value = max(findSum(r+1,c-1), findSum(r+1,c), findSum(r+1,c+1)) + int(matrix[r*n + c])
    memo[(r,c)] = value
    return value

for l in range(testCases):
    n = int(inputLines.readline())
    matrix = inputLines.readline().strip().split()
    memo = {}
    maximum = 0

    for i in range(n):
        val = findSum(0,i)
        if(val > maximum):
            maximum = val

    print(maximum)
