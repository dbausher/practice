"http://practice.geeksforgeeks.org/problems/head-to-tail-ordering/0"

import fileinput
import collections

alphabet = "abcdefghijklmnopqrstuvwkyz"
letterNumber = {alphabet[i]:i for i in range(26)}

def wordyCheck(n, words):
    if(len(words) <= 1):
        return "Head to tail ordering is possible."

    adjacency = [[0 for i in range(26)] for i in range(26)]
    ones = 0
    negones = 0
    connected = collections.defaultdict(bool)
    columnSum = collections.defaultdict(int)
    rowSum = collections.defaultdict(int)
    relevant = []
    connections = collections.defaultdict(set)

    for word in words:
        firstLetterNumber = letterNumber[word[0]]
        lastLetterNumber = letterNumber[word[len(word) - 1]]

        adjacency[firstLetterNumber][lastLetterNumber] += 1
        connections[firstLetterNumber].add(lastLetterNumber)
        connections[lastLetterNumber].add(firstLetterNumber)


    for i in range(26):
        for j in range(26):
            rowSum[i] += adjacency[i][j]
            columnSum[i] += adjacency[j][i]

    for k in range(26):
        if(adjacency[k][k] > 0 and not (rowSum[k] > adjacency[k][k] or columnSum[k] > adjacency[k][k])):
            return "Head to tail ordering is not possible."
        degreeDiff = (rowSum[k] - columnSum[k])

        if(degreeDiff > 1 or degreeDiff < -1):
            return "Head to tail ordering is not possible."
        if(degreeDiff == 1):
            ones += 1
        if(degreeDiff == -1):
            negones += 1

        if(rowSum[k] > 0 or columnSum[k] > 0):
            relevant.append(k)

    if(ones + negones > 0 and not (ones == 1 and negones == 1)):
        return "Head to tail ordering is not possible."

    toConnect = [relevant[0]]
    connected[relevant[0]] = True

    while toConnect:
        curr = toConnect.pop()
        for reachable in connections[curr]:
            if(not connected[reachable]):
                connected[reachable] = True
                toConnect.append(reachable)

    for letter in relevant:
        if not connected[letter]:
            return "Head to tail ordering is not possible."

    return "Head to tail ordering is possible."

inputLines = fileinput.input()

testCases = int(inputLines.readline())

for l in range(testCases):
    n = int(inputLines.readline())
    words = []
    for i in range(n):  
        words.append(inputLines.readline().strip())
    print(wordyCheck(n,words))