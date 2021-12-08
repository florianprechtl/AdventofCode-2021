from utils import readLines, readInput

def challenge_1():
    input = readInput('input.txt')
    lines = readLines(input)
    numbers = [int(line) for line in lines[0].split(",")]

    for _ in range(80):
        countNewFish = 0
        for i,number in enumerate(numbers):
            if number == 0:
                numbers[i] = 6
                countNewFish += 1
            else:
                numbers[i] -= 1
        for _ in range(countNewFish):
            numbers.append(8)
        # print(numbers)

    print(len(numbers))
