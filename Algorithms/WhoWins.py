"""http://practice.geeksforgeeks.org/problems/who-will-win/0"""

import fileinput
import math

inputLines = fileinput.input()

testCases = int(inputLines.readline())

for l in range(testCases):
    N,M,G,S = list(map(int,inputLines.readline().strip().split()))
    i = N//2
    searches = 1

    while(i > 0):
        if M%i == 0:
            break
        searches+=1
        i = i//2

    gtime = M*G
    stime = S*searches
    if(gtime < stime):
        print(1)
    elif(gtime > stime):
        print(2)
    else:
        print(0)
