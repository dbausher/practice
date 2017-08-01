"""http://practice.geeksforgeeks.org/problems/implementing-floyd-warshall/0"""

import fileinput

inputLines = fileinput.input()

testCases = int(inputLines.readline())

for l in range(testCases):

    #weights[i][j] (i and j 1-indexed) -> #weights[V*(i-1) + (j-1)]
    #weights[i][j] (i and j 0-indexed) -> #weights[V*(i) + (j)]

    V =  int(inputLines.readline())
    weights = list(map(int,inputLines.readline().split()))
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if(weights[V*i + j]  > weights[V*i + k] + weights[V*k + j]):
                    weights[V*i + j]  = weights[V*i + k] + weights[V*k + j]
    print(" ".join(list(map(str,weights))))