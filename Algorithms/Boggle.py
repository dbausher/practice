"""http://practice.geeksforgeeks.org/problems/word-boggle/0"""

import fileinput
import collections

inputLines = fileinput.input()

testCases = int(inputLines.readline())

def dfs(location,word,used):
    used[location] = True
    if(word in dictionary):
        dictionary[word] = True

    adjacent = (location + 1, location - 1, location + n, location - n, location + n + 1, location + n -1, location -n +1, location -n -1)
    for place in adjacent:
        if(place >= 0 and place < m*n and not used[place]):
            dfs(place,word + boggle[place], used.copy())

for testCase in range(testCases):
    wordLength = int(inputLines.readline())
    wordList = inputLines.readline().split()
    dictionary = {}
    for word in wordList:
        dictionary[word] = False

    n,m = tuple(map(int,inputLines.readline().split()))
    boggle = inputLines.readline().split()

    for i in range(len(boggle)):
        dfs(i,"",collections.defaultdict(bool))

    finalWord = []

    for word in wordList:
        if(dictionary[word]):
            finalWord.append(word)

    if(len(finalWord) > 0):
        finalWord.sort()
        print( " ".join(finalWord))
    else:
        print(-1)
