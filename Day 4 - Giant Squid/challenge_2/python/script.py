import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, '../input.txt'), 'r')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printBingoField(bingoField):
    for y in range(len(bingoField)):
        for x in range(len(bingoField[0])):
            if (bingoField[y][x] in calledNumbers):
                print(f"{bcolors.WARNING}{str(bingoField[y][x]).ljust(2)}{bcolors.ENDC}", end='')
            else:
                print(str(bingoField[y][x]).ljust(2), end='')
            
            if (x != (len(bingoField[0]) - 1)):
                print(" ", end='')
        print("") 
    print("")

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

foundbingoFieldIndices = []

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
    currentBingoIndex = 0
    print(f"--- new Number {number} ---")
    for index, bingoField in enumerate(allBingoFields):
        if (index in foundbingoFieldIndices):
            continue
        printBingoField(bingoField)
        currentBingoIndex = index
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
            foundBingo = False
            if currentBingoIndex not in foundbingoFieldIndices:
                foundbingoFieldIndices.append(currentBingoIndex)
                if (len(foundbingoFieldIndices) == len(allBingoFields)):
                    print(number)

    

print(foundbingoFieldIndices)