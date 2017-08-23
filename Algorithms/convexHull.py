"""http://practice.geeksforgeeks.org/problems/gcd-of-array/0"""

import fileinput
import math
import functools

inputLines = fileinput.input()

testCases = int(inputLines.readline())

def slope(a,b):
    if(b[0] == a[0]):
        return 1001
    return (b[1]-a[1])/(b[0]-a[0])
def turn(p,q,r):
    return (q[0] - p[0])*(r[1] - p[1]) - (q[1] - p[1])*(r[0] - p[0])

def angle(p,q,r):
    v1 = q-p
    v2 = r-q
    num = v1[0]*v2[0] + v1[1]*v2[1]
    den = math.sqrt(pow(v1[0],2) + pow(v1[1],2))*math.sqrt(pow(v2[0],2) + pow(v2[1],2))
    return math.acos(den)

for l in range(testCases):
    n = int(inputLines.readline())
    numList = list(map(int,inputLines.readline().strip().split()))
    xyd = list(zip(numList[::2],numList[1::2]))
    first = min(xyd)
    out = list()
    out.append(first)
    xyd.sort(key = lambda x:slope(first,x))

    for i in range(0,n):
        if(xyd[i] == first):
            break
        for j in range(0,n):
            if(i != j and turn(out[-1],xyd[i],xyd[j]) < 0):
                break
        else:
            out.append(xyd[i])

    if(n < 3 or len(out) < 3):
        print("-1")
    else:
        out.sort()
        outstring = ", ".join(list(map(lambda x : str(x[0]) + " " + str(x[1]), out)))
        print(outstring)



