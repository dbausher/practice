"""http://practice.geeksforgeeks.org/problems/subset-sum-problem/0"""
import fileinput

inputLines = fileinput.input()

testCases = int(inputLines.readline())

def EqualSum(l1sum,curr):
    if((l1sum,curr) in memo):
        return memo[(l1sum,curr)]
    diff = sumBoy - 2*l1sum
    if(not diff):
        return True
    elif curr == n or diff < 0 or diff/2 > suffixSum[curr]:
        return False
    else:
        worked = (EqualSum(l1sum,curr + 1) or EqualSum(l1sum + listboy[curr],curr+1))
        memo[(l1sum,curr)] = worked
        return worked

for l in range(testCases):
    n = int(inputLines.readline())
    listboy = list(map(int, inputLines.readline().strip().split()))
    sumBoy = sum(listboy)
    memo = {}
    suffixSum = [sum(listboy[i:]) for i in range(n)]
    if(sumBoy%2):
        print("NO")
    else:
        if(EqualSum(0,0)):
            print("YES")
        else:
            print("NO")
