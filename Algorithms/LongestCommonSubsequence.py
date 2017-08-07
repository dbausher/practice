"""http://practice.geeksforgeeks.org/problems/longest-common-subsequence/0"""

import fileinput

def LCSS(s1, s2):
    if((s1,s2) not in longest):
        if(not s1 or not s2):
            longest[(s1,s2)] = 0
        elif(s1[len(s1) - 1] == s2[len(s2) - 1]):
            longest[(s1,s2)] = LCSS(s1[:len(s1) - 1],s2[:len(s2) - 1]) + 1
        else:
            longest[(s1,s2)] = max(LCSS(s1[:len(s1) - 1],s2), LCSS(s1,s2[:len(s2) - 1]))
    return longest[(s1,s2)]

inputLines = fileinput.input()

testCases = int(inputLines.readline())

for l in range(testCases):

    wordLengths = inputLines.readline()
    string1 = inputLines.readline().strip()
    string2 = inputLines.readline().strip()

    longest = {}

    print(LCSS(string1, string2))