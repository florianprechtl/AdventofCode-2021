from utils import readLines, readInput

def challenge_2():
    input = readInput('input.txt')
    lines = readLines(input)
    numbers = [int(line) for line in lines[0].split(",")]

    numberCounts = [0 for _ in range(9)]

    for number in numbers:
        numberCounts[number]+=1

    for _ in range(256):
        newNumberCounts = [0 for _ in range(9)]
        for i,numberCount in enumerate(numberCounts):
            if i == 0:
                newNumberCounts[6] += numberCount
                newNumberCounts[8] += numberCount
            else:
                newNumberCounts[i-1] += numberCount
        # print(numbers)
        numberCounts = newNumberCounts


    result = 0
    for i in range(9):
        result += numberCounts[i]
    print(result)