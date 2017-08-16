"""http://practice.geeksforgeeks.org/problems/kth-smallest-element/0"""

import fileinput
import math

inputLines = fileinput.input()

testCases = int(inputLines.readline())

def quickSelect(l,low,high):
    if low < high:
        mid = partition(l,low,high)
        if(mid == k - 1):
            return
        elif(mid > k -1):
            quickSelect(l,low,mid-1)
        else:
            quickSelect(l,mid+1,high)
        
        

def partition(l,low,high):
    pivot = l[high]
    prev = low
    for i in range(low,high):
        if(l[i] <= pivot ):
            l[prev],l[i] = l[i],l[prev]
            prev += 1
    l[prev],l[high] = l[high],l[prev]
    return prev


for l in range(testCases):
    n = int(inputLines.readline())
    numList = list(map(int,inputLines.readline().strip().split()))
    k = int(inputLines.readline())
    quickSelect(numList,0,n-1)
    print(numList[k-1])