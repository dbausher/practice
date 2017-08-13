"""http://practice.geeksforgeeks.org/problems/search-in-a-rotated-array/0"""

import fileinput
import math

inputLines = fileinput.input()

testCases = int(inputLines.readline())

def binarySearch(l,start,end,target):
    if(end <= start + 1):
        if(l[start] == target):
            return start
        elif(l[end] == target):
            return end
        else:
            return -1
    half = (start+end)//2
    if(l[half] == target):
        return half
    elif(l[half] > target):
        return binarySearch(l,start,half,target)
    else:
        return binarySearch(l,half,end,target)

def pivotSearch(l,start,end):
    half = (start+end)//2
    if(l[half + 1] < l[half]):
        return half + 1
    if(start == end):
        if(end < len(l) -1 and l[end] < l[end] + 1):
            return end + 1
        elif(l[start] < l[start + 1]):
            return start + 1
        else:
            return -1
    if l[half] < final:
        return pivotSearch(l,start,half)
    return pivotSearch(l,half,end)


for l in range(testCases):
    n = int(inputLines.readline())
    rotated = list(map(int,inputLines.readline().strip().split()))
    key = int(inputLines.readline())
    final = rotated[n - 1]
    if(final > rotated[0]):
        print(binarySearch(rotated,0,n-1,key))
        continue
    rotationPoint = pivotSearch(rotated,0,n-1)
    if(final > key):
        rightSide = rotated[rotationPoint:n]
        location = binarySearch(rightSide,0,len(rightSide) - 1,key)
        if(location > -1):
            print(rotationPoint + location)
        else:
            print(location)
    else:
        leftSide = rotated[0:rotationPoint]
        print(binarySearch(leftSide,0,rotationPoint -1,key))
