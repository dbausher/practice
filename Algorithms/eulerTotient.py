"""http://practice.geeksforgeeks.org/problems/euler-totient/0"""

import fileinput
import math

inputLines = fileinput.input()

testCases = int(inputLines.readline())

def euclid(a,b):
    while b:
        a,b = b,a%b
    return a

def mods(x):
    factors = set()
    for i in range(1,int(math.sqrt(x) + 1)):
        if(x%i == 0):
            factors.add(i)
            if not i==1:
                factors.add(x//i)
    return factors
    
def prime_factors(x):
    primes = set()
    if x%2 == 0:
        primes.add(2)
    while x%2 == 0:
        x /= 2
    for k in range(3,int(math.sqrt(x) + 1),2):
        if x %k == 0:
            primes.add(k)
        while x%k == 0:
            x /= k
    if x != 1:
        primes.add(x)
    return primes

for l in range(testCases):
    n = int(inputLines.readline())
    biggest = pow(10,12)
    biggestSource = 0
    for i in range(1,n + 1):
        pi = 1
        for j in prime_factors(i):
            pi *= (1-1/j)
            # if(pi > biggest):
            #     break

        if(pi < biggest):
            biggest = pi
            biggestSource = i

    print(biggestSource)
