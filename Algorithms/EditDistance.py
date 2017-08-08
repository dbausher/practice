"""http://practice.geeksforgeeks.org/problems/edit-distance/0"""

import fileinput
import collections

inputLines = fileinput.input()

testCases = int(inputLines.readline())

def ED(w1,w2):
    if((w1,w2) in memo):
        return memo[(w1,w2)]
    if not w1:
        value = len(w2)
    elif not w2:
        value = len(w1)
    elif(w1[len(w1) -1] == w2[len(w2) -1]):
        value = ED(w1[:len(w1) -1],w2[:len(w2) -1])
    else:
        value = min(ED(w1,w2[:len(w2) -1]), ED(w1[:len(w1) -1],w2), ED(w1[:len(w1) -1],w2[:len(w2) -1])) + 1
    memo[(w1,w2)] = value
    return value

for l in range(testCases):
    wordLengths = inputLines.readline().split()
    words = inputLines.readline().split()
    memo = {}
    memo[""] = 0

    print(ED(words[0],words[1]))
