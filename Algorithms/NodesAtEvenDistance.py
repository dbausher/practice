import fileinput
from collections import deque

inputLines = fileinput.input()

testCases = int(inputLines.readline())

for l in range(testCases):

    n = int(inputLines.readline())

    adjacency = [[-1 for i in range(n)] for j in range(n)]

    splitEdges = list(map(int,inputLines.readline().split()))

    for i in range(2*(n-1)):
        if(i%2 == 0):
            adjacency[splitEdges[i]-1][splitEdges[i+1]-1] = 0
            adjacency[splitEdges[i+1]-1][splitEdges[i]-1] = 0


    s = [0]

    while(len(s) > 0):
        curr = s.pop()
        for i in range(n):
            if(i == curr):
                adjacency[curr][curr] = 0
            elif(adjacency[curr][i] == 0 and adjacency[0][i] < 1):
                adjacency[0][i] = adjacency[0][curr] + 1
                s.append(i)

    odds = 0.0
    evens = 0.0

    for k in range(n):
        if(adjacency[0][k]%2 == 0):
            evens += 1.0
        else:
            odds += 1.0
    print(int((odds*(odds-1))/2 + ((evens-1)*evens)/2)) 
	
