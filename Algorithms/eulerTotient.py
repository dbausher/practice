"""http://practice.geeksforgeeks.org/problems/euler-totient/0"""
# phi(m) = m*pi(prime_factors(m))
# phi(m*n) = m*n*pi(prime_factors(m))*pi(prime_factors(n))
# max(m*n/phi(m*n)) == min(pi(prime_factors(m))*pi(prime_factors(n))

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

def pi(x):
    origx = x
    curr = 1
    if x in pis:
        return pis[x]
    if x%2 == 0:
        if euclid(x//2,2) == 1:
            pis[x] = pis[2] * pis[x//2]
            return pis[x]
    else:
        for k in range(3,int(math.sqrt(x) + 1),2):
            if x %k == 0 and euclid(x//k,k) == 1:
                pis[x] = pis[k] * pis[x//k]
                return pis[x]
    if x%2 == 0:
        curr *= 1/2.0
        while x%2 == 0:
            x /= 2
    for k in range(3,int(math.sqrt(x)) + 1,2):
        if x%k == 0:
            curr *= 1 - (1/k)
        while x%k == 0:
            x/= k
    if x > 1:
        curr *= 1-(1/x)
    pis[origx] = curr
    return pis[origx]


for l in range(testCases):
    n = int(inputLines.readline())
    pis = {2:.5,3:2.0/3.0}
    biggest = pow(10,12)
    biggestSource = 1
    for i in range(2,n + 1):
        pis[i] = pi(i)
        pii = pis[i]


        if(pii < biggest):
            biggest = pii
            biggestSource = i

    print(biggestSource)
