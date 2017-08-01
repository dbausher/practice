"""http://practice.geeksforgeeks.org/problems/x-total-shapes/0"""

import fileinput
from collections import deque

inputLines = fileinput.input()

testCases = int(inputLines.readline())

for testCase in range(testCases):
	dimensions = list(map(int ,inputLines.readline().split()))
	matrix = inputLines.readline().split()

	visited = [[False for x in range(int(dimensions[1]))]for y in range(int(dimensions[0]))]
	totalX = 0
	for i in range(dimensions[0]):
		for j in range(dimensions[1]):
			if(visited[i][j]):
				continue
			visited[i][j] = True
			if(matrix[i][j] == 'X'):
				q = deque([(i,j)])
				while len(q) > 0:
					k,l = q.pop()
					visited[k][l] = True
					adjacencies = [(k-1,l), (k, l-1), (k+1, l), (k,l+1)]
					for point in adjacencies:
						if(point[0] >= 0 and point[0] < dimensions[0] and point[1] >= 0 and point[1] < dimensions[1] and matrix[point[0]][point[1]] == 'X' and not visited[point[0]][point[1]]):
							q.appendleft(point)
				totalX += 1
	print(totalX)
