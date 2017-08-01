import fileinput

inputLines = fileinput.input()

testCases = int(inputLines.readline())

for l in range(testCases):
    n = int(inputLines.readline())

    length = 0

    while(n > 2):
        n, r = divmod(n,3)
        length += r + 1

    if(n == 2):
        length += 1
        

    print(length)



def greedySearch(n):
    length = 0

    while(n > 2):
        n, r = divmod(n,3)
        length += r + 1

    if(n == 2):
        length += 1

    return length