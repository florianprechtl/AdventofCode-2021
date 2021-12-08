from utils import readLines, readInput

def challenge_2():
    input = readInput('input.txt')
    lines = readLines(input)
    numbers = [int(line) for line in lines[0].split(",")]

    minSum = 100000000
    minNum = 100000
    currSum = 0

    for i in range(0, max(numbers)):
        for number in numbers:
            diff = abs(number - i)
            realDist = sum(range(0,diff+1))
            currSum += realDist
        if currSum < minSum:
            minSum = currSum
            minNum = i
        currSum = 0
        

    print("MinNum: ", minNum)
    print("MinSum: ", minSum)
