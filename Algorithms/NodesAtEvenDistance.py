"""http://practice.geeksforgeeks.org/problems/nodes-at-even-distance/0"""

import fileinput

inputLines = fileinput.input()

testCases = int(inputLines.readline())

for l in range(testCases):

    n = int(inputLines.readline())

    adjacency = {i : [] for i in range(n)}
    visited = {}
    splitEdges = list(map(int,inputLines.readline().split()))

    for i in range(2*(n-1)):
        if(not i%2):
            adjacency[splitEdges[i] - 1].append(splitEdges[i+1]-1)
            adjacency[splitEdges[i+1]-1].append(splitEdges[i] - 1)



        
    evens = {True : 1, False: 0}

    s = [(0,True)]

    while(len(s) > 0):
        curr, even = s.pop()
        for other in adjacency[curr]:
            if(not adjacency[other] == None):
                evens[not even] += 1
                s.append((other, not even))
        adjacency[curr] = None

    
    print(int((evens[True]*(evens[True]-1))/2 + ((evens[False]-1)*evens[False])/2))
	
