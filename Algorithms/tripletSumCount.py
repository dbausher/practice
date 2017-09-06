"""http://www.geeksforgeeks.org/count-triplets-with-sum-smaller-that-a-given-value/"""

import fileinput

inputLines = fileinput.input()


#I didn't manage to solve this one. I looked it up after staring for about an hour.

#Also its currently n^2 and doesn't pass so I'm shelving this one for a day when I've slept.
#Turns out it passes if i just put the whole thing in a function so *shrug*

testCases = int(inputLines.readline())
for l in range(testCases):
    n, s = list(map(int,inputLines.readline().strip().split()))
    numList = list(sorted(map(int,inputLines.readline().strip().split())))
    #numList.sort()

    count = 0

    for i, v in enumerate(numList):
        if v + numList[0] >= s:
            break
        s2 = s - v
        j = i + 1
        k = n - 1
        while j < k:
            if numList[j] + numList[k] < s2:
                count += k - j
                j += 1
            else:
                k -= 1

    print(count)