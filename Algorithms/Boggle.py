"""http://practice.geeksforgeeks.org/problems/word-boggle/0"""

import fileinput
import collections

inputLines = fileinput.input()

testCases = int(inputLines.readline())


def dfs(location,word,used,trie):
    used[location] = True
    if("end" in trie):
        finalWord.add(word)
    adjacent = (location + 1, location - 1, location + n, location - n, location + n + 1, location + n -1, location -n +1, location -n -1)
    for place in adjacent:
        if(place >= 0 and place < m*n and boggle[place] in trie and not used[place]):
            dfs(place,word + boggle[place], used.copy(), trie[boggle[place]])

for testCase in range(testCases):
    wordLength = int(inputLines.readline())
    wordList = inputLines.readline().split()
    finalWord = set()
    trie = {}
    for word in wordList:
        current = trie
        for letter in word:
            current = current.setdefault(letter, {})
        current["end"] = "end"


    m,n = tuple(map(int,inputLines.readline().split()))
    boggle = inputLines.readline().split()

    for i in range(len(boggle)):
        if(boggle[i] in trie):
            dfs(i,boggle[i],collections.defaultdict(bool),trie[boggle[i]])

    if(len(finalWord) > 0):
        finalWordList = list(finalWord)
        finalWordList.sort()
        print( " ".join(finalWordList))
    else:
        print(-1)
