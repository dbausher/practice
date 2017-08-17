"""http://practice.geeksforgeeks.org/problems/preorder-to-postorder/0"""

import fileinput
import math

inputLines = fileinput.input()

testCases = int(inputLines.readline())

class node: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(l,pos,minimum = 0,maximum = 1001):
    me = node(l[pos])
    curr = pos
    curr += 1
    if(curr < n and l[curr] < me.data and l[curr] > minimum):
        me.left,curr = buildTree(l,curr,minimum,me.data)
    if(curr < n and l[curr] > me.data and l[curr] < maximum):
        me.right,curr = buildTree(l,curr,me.data,maximum)
    return (me,curr)

def postOrder(root,l):
    if(root):
        postOrder(root.left,l)
        postOrder(root.right,l)
        l.append(root.data)

for l in range(testCases):
    n = int(inputLines.readline())
    numList = list(map(int,inputLines.readline().strip().split()))
    root,length = buildTree(numList,0)
    newList = []
    postOrder(root,newList)
    if(len(newList) < n):
        print("NO")
    else:
        print(" ".join(list(map(str,newList))))