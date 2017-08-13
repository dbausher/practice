"""http://practice.geeksforgeeks.org/problems/tom-and-jerry/0"""



import fileinput
import math

inputLines = fileinput.input()

testCases = int(inputLines.readline())

def ways(start,end,truth):
    if(start == end):
        if(fullStatement[start] == "T"):
            return int(truth)
        return int(not truth)
    if((start,end,truth) in  memo):
        return memo[start,end,truth]
    value = 0
    for i in range(start,end,2):
        op = fullStatement[i + 1]
        if(op == '&'):
            if truth:
                value += ways(start,i,True)*ways(i+2,end,True)
            else:
                value += (ways(start,i,True) + ways(start,i,False))*(ways(i+2,end,True) + ways(i+2,end,False))
                value -= ways(start,i,True)*ways(i+2,end,True)
        elif(op == '|'):
            if truth:
                value += (ways(start,i,True) + ways(start,i,False))*(ways(i+2,end,True) + ways(i+2,end,False))
                value -= ways(start,i,False)*ways(i+2,end,False)
            else:
                value += ways(start,i,False)*ways(i+2,end,False)
        elif(op == '^'):
            if truth:
                value += ways(start,i,True)*ways(i+2,end,False)
                value += ways(start,i,False)*ways(i+2,end,True)
            else:
                value += ways(start,i,True)*ways(i+2,end,True)
                value += ways(start,i,False)*ways(i+2,end,False)
    memo[start,end,truth] = value
    return value

for l in range(testCases):
    n = int(inputLines.readline())
    fullStatement = inputLines.readline().strip()
    memo = {}

    print(ways(0,n - 1,True)%1003)
