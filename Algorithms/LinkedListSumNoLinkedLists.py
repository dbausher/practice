import fileinput
import collections

inputLines = fileinput.input()

testCases = int(inputLines.readline())

for testCase in range(testCases):
    lengthStrings = inputLines.readline()
    number1 = int("".join(inputLines.readline().split()))
    number2 = int("".join(inputLines.readline().split()))
    summed = number2 + number1
    print(" ".join(list(str(summed))))