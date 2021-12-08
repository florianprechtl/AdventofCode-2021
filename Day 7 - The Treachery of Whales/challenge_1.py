from utils import readLines, readInput
import math

def challenge_1():
    input = readInput('input.txt')
    lines = readLines(input)
    numbers = [int(line) for line in lines[0].split(",")]

    minSum = 100000000
    minNum = 100000
    currSum = 0


    for i in range(0, max(numbers)):
        for number in numbers:
            currSum += abs(number - i)
        if currSum < minSum:
            minSum = currSum
            minNum = i
        currSum = 0
        

    print("MinNum: ", minNum)
    print("MinSum: ", minSum)
