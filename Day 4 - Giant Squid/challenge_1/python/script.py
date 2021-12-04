import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, '../input.txt'), 'r')

text = f.read()
text = text.replace("  ", " ")
text = text.replace("  ", " ")
lines = text.split("\n")
lines = [line.strip() for line in lines]

allNumbers = [int(number) for number in lines[0].split(",")]
allBingoFields = []
calledNumbers = []

startSetoff = 2
bingoIndex = 0
currentIndex = (startSetoff + bingoIndex * 6)

while (currentIndex < len(lines)):
    bingoFieldAsLines = lines[currentIndex:currentIndex+5:1]
    bingoField = []
    for i in range(len(bingoFieldAsLines)):
        numbers = bingoFieldAsLines[i].split(" ")
        numbers = [int(num) for num in numbers]
        bingoField.append(numbers)
    bingoIndex += 1
    allBingoFields.append(bingoField)
    currentIndex = (startSetoff + bingoIndex * 6)

foundBingo = False

for number in allNumbers:
    calledNumbers.append(number)
    for bingoField in allBingoFields:
        # search rows
        for y in range(len(bingoField)):
            broken = False
            for x in range(len(bingoField[0])):
                currNumCheck = bingoField[y][x]
                numberIsNotCalled = not currNumCheck in calledNumbers
                if (numberIsNotCalled):
                    broken = True
                    break
            if (not broken):
                flat_list = [item for sublist in bingoField for item in sublist]
                missingSum = sum([n for n in flat_list if not n in calledNumbers])
                result = number * missingSum
                print("found bingo :", missingSum, " * ", number, " = ", result)
                foundBingo = True
                break
        if (foundBingo):
            break
            

        # search columns
        for x in range(len(bingoField[0])):
            broken = False
            for y in range(len(bingoField)):
                currNumCheck = bingoField[y][x]
                numberIsNotCalled = not currNumCheck in calledNumbers
                if (numberIsNotCalled):
                    broken = True
                    break
            if (not broken ):
                flat_list = [item for sublist in bingoField for item in sublist]
                missingSum = sum([n for n in flat_list if not n in calledNumbers])
                result = number * missingSum
                print("found bingo :", missingSum, " * ", number, " = ", result)
                foundBingo = True
                break
        if (foundBingo):
            break

    if (foundBingo):
            break